from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.db.models import Sum
from django.shortcuts import render, redirect
from .forms import *
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from string import digits, ascii_lowercase, ascii_uppercase
from random import choice


# Create your views here.

class IndexView(DataMixin, ListView):
    template_name = 'shop/index.html'
    model = Categories
    context_object_name = 'catalog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class InfoAboutView(DataMixin, TemplateView):
    template_name = 'shop/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class CategoryGoodsView(DataMixin, ListView):
    template_name = 'shop/goods.html'
    model = Goods
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(cat_name=self.kwargs['category'])
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Goods.objects.filter(category__slug=self.kwargs['category'])


class GoodInfoView(DataMixin, DetailView, FormView):
    model = Goods
    template_name = 'shop/info_good.html'
    slug_url_kwarg = 'good'
    context_object_name = 'good'
    form_class = AddGoodForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        if self.request.user.is_anonymous:
            return redirect('shop_profile')
        quantity = form.cleaned_data['quantity']
        good_slug = self.kwargs['good']
        good = Goods.objects.get(slug=good_slug)
        user = self.request.user
        price = Goods.objects.get(slug=good_slug).price
        cost = quantity * price
        currency = good.currency
        ShoppingCart.objects.create(user=user, good=good, quantity=quantity, price=price, cost=cost, currency=currency)
        return redirect(self.request.path)


class DoneView(TemplateView):
    template_name = 'shop/done.html'


class RegistrationView(DataMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'shop/registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('shop_index')


class LoginProfileView(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'shop/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('shop_profile')


class ServiceView(DataMixin, CreateView):
    model = Defects
    template_name = 'shop/service.html'
    success_url = '/done/'
    form_class = ServiceForm
    login_url = 'shop_profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class ContactView(DataMixin, CreateView):
    form_class = ContactForm
    template_name = 'shop/contact.html'
    success_url = '/done/'
    model = Messages

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class ShoppingCartView(LoginRequiredMixin, DataMixin, FormView):
    template_name = 'shop/shopping_cart.html'
    login_url = 'shop_profile'
    form_class = CartForm
    success_url = '/done/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_cart = ShoppingCart.objects.filter(user=self.request.user).select_related('good')
        total = profile_cart.aggregate(Sum('cost'))['cost__sum']
        c_def = self.get_user_context(profile_cart=profile_cart, total=total, user=self.request.user)
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        phone = form.cleaned_data['phone']
        delivery_address = form.cleaned_data['delivery_address']
        user = self.request.user
        total = ShoppingCart.objects.filter(user=user).aggregate(Sum('cost'))['cost__sum']
        Orders.objects.create(user=user, total=total, delivery_address=delivery_address, phone=phone)
        order = Orders.objects.filter(user=user).last()
        for g in ShoppingCart.objects.filter(user=user):
            good = g.good
            quantity = g.quantity
            price = g.price
            cost = g.cost
            currency = g.currency
            OrderDetails.objects.create(order=order, user=user, good=good, quantity=quantity,
                                        price=price, cost=cost, total=total, currency=currency)
        clear_cart(self.request, user.id)
        return redirect('shop_done')


def clear_cart(request, id):
    ShoppingCart.objects.filter(user=id).delete()
    return redirect('shop_cart')


class ForgotPasswordView(FormView):
    form_class = ForgotPasswordForm
    template_name = 'shop/forgot_password.html'
    success_url = '/done/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        all_emails = [obj.email for obj in User.objects.all()]
        if email not in all_emails:
            return redirect('shop_wrong')
        else:
            new_password = ''.join(str(choice(k)) for _ in range(3) for k in (digits, ascii_lowercase, ascii_uppercase))
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            # send_to_email
        return redirect('shop_done')


class IncorrectEmailView(TemplateView):
    template_name = 'shop/incorrect_email.html'


