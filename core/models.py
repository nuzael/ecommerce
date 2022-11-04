from django_extensions.db.fields import AutoSlugField
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.db import models


GENDER_CHOICES = (
    ('T', 'Todos'),
    ('M', 'Masculino'),
    ('F', 'Feminino')
)

CATEGORY_CHOICES = (
    ('CAMISETA', 'Camiseta'),
    ('CALCA', 'Calça'),
    ('TENIS', 'Tênis'),
    ('OCULOS', 'Óculos'),
    ('RELOGIO', 'Relógio')
)


class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand_images')
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='product_images')
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    specification = models.TextField(blank=True)
    size = models.CharField(max_length=100, blank=True)
    slug = AutoSlugField(populate_from=['title', 'brand', 'color', 'randomid'])
    quantity = models.IntegerField(default=1)
    
    def randomid(self):
        return get_random_string(length=12)
    
    def __str__(self):
        return self.title
    
    
class ProductImage(models.Model): 
    name = models.CharField(max_length=255) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.name
    
    
class OrderProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.product.title


class FavoriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)

    def __str__(self):
        return self.user.username