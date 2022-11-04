from django.contrib import admin
from .models import Product, ProductImage, Brand, OrderProduct, Order, FavoriteProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'brand', 'category', 'size', 'quantity')
    
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'image')
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name')

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')

class FavoriteProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')
    

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
admin.site.register(FavoriteProduct, FavoriteProductAdmin)
admin.site.register(Order)
