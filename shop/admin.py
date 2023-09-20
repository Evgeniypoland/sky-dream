from django.contrib import admin
from .models import *


# Register your models here.
class PriceFilter(admin.SimpleListFilter):
    title = 'Price range'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return [('less 1000', '<1000'),
                ('from 1000 to 2000', '1000-2000'),
                ('from 2000 to 3000', '2000-3000'),
                ('greater 3000', '>3000')]

    def queryset(self, request, queryset):
        if self.value() == 'less 1000':
            return queryset.filter(price__lt=1000)
        elif self.value() == 'from 1000 to 2000':
            return queryset.filter(price__gte=1000).filter(price__lt=2000)
        elif self.value() == 'from 2000 to 3000':
            return queryset.filter(price__gte=2000).filter(price__lt=3000)
        elif self.value() == 'greater 3000':
            return queryset.filter(price__gte=3000)


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'currency', 'category', 'description', 'image']
    list_editable = ['description', 'price', 'currency']
    ordering = ['price']
    actions = ['set_dollar', 'set_euro']
    search_fields = ['name', 'description']
    list_filter = ['currency', PriceFilter, 'category']
    prepopulated_fields = {'slug': ('name',)}

    @admin.action(description='Set currency dollar')
    def set_dollar(self, request, qs):
        count = qs.update(currency=Goods.USD)
        self.message_user(request, f'{count} currency updated')

    @admin.action(description='Set currency euro')
    def set_euro(self, request, qs):
        count = qs.update(currency=Goods.EUR)
        self.message_user(request, f'{count} currency updated')


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    search_fields = ['name', 'email', 'message']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'description', 'photo']
    search_fields = ['name', 'email', 'description', 'phone']


class MainPageGalleryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']


class SalesAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'new_price']


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'good', 'quantity', 'price', 'cost', 'currency']
    list_filter = ['user']
    search_fields = ['user__username', 'good__name']


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['order', 'user', 'good', 'quantity', 'price', 'cost', 'total', 'currency']
    list_filter = ['user']
    search_fields = ['order__id', 'good__name', 'user__username']


class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total', 'delivery_address', 'phone', 'order_date']
    list_filter = ['user']
    search_fields = ['id', 'user__username', 'delivery_address', 'phone', 'order_date']


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Categories)
admin.site.register(Messages, MessageAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Defects, ServiceAdmin)
admin.site.register(MainPageGallery, MainPageGalleryAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(ShoppingCart, CartAdmin)
