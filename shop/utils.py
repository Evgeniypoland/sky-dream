from .models import *
from random import choice

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['picture'] = choice(MainPageGallery.objects.all())
        context['catalog'] = Categories.objects.all()
        context['sales'] = Sales.objects.all().select_related('name')
        return context


