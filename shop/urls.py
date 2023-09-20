from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='shop_index'),
    path('profile/', views.LoginProfileView.as_view(), name='shop_profile'),
    path('profile/forgotpassword/', views.ForgotPasswordView.as_view(), name='shop_forgot_password'),
    path('logout/', views.logout_user, name='shop_logout'),
    path('profile/registration/', views.RegistrationView.as_view(), name='shop_registration'),
    path('shopping_cart/', views.ShoppingCartView.as_view(), name='shop_cart'),
    path('about_us/', views.InfoAboutView.as_view(), name='shop_about_us'),
    path('service/', views.ServiceView.as_view(), name='shop_service'),
    path('contact/', views.ContactView.as_view(), name='shop_contact'),
    path('wrong/', views.IncorrectEmailView.as_view(), name='shop_wrong'),
    path('done/', views.DoneView.as_view(), name='shop_done'),
    path('clear_cart/<id>/', views.clear_cart, name='shop_clear_cart'),
    path('<slug:category>/', cache_page(60)(views.CategoryGoodsView.as_view()), name='shop_category'),
    path('<slug:category>/<slug:good>/', cache_page(60)(views.GoodInfoView.as_view()), name='shop_good'),
]
