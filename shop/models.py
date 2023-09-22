from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(default='', db_index=True, null=False)

    def __str__(self):
        return f'{self.name}'


class Goods(models.Model):
    USD = '$'
    EUR = '€'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars')
    ]
    name = models.CharField(max_length=30, unique=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=1, choices=CURRENCY_CHOICES, default='$')
    slug = models.SlugField(default='', db_index=True, null=False)
    image = models.ImageField(upload_to='catalog', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Messages(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(1)])
    email = models.EmailField(max_length=100)
    message = models.TextField(validators=[MinLengthValidator(1)])


class Defects(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    description = models.TextField()
    photo = models.FileField(upload_to='uploads/defect_photos')


class MainPageGallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/main page gallery', null=True, blank=True)


class Sales(models.Model):
    name = models.OneToOneField(Goods, on_delete=models.CASCADE)
    new_price = models.IntegerField()
    image = models.ImageField(upload_to='static/sales')


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    cost = models.IntegerField()
    currency = models.CharField(max_length=1, default='$')


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    delivery_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'


class OrderDetails(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    cost = models.IntegerField()
    total = models.IntegerField()
    currency = models.CharField(max_length=1, default='$')

# python manage.py shell_plus --print-sql
