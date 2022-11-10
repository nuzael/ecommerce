from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import Product, ProductImage, Brand, Category, OrderProduct, FavoriteProduct


def quantity_of_items(request):
    if request.user.is_authenticated:
        quantity = 0
        for product in OrderProduct.objects.filter(user=request.user):
            quantity += product.quantity  
    else:
        quantity = 0
    return quantity

def index(request):
    cart_quantity = quantity_of_items(request)
    categories = Category.objects.all()
        
    # Arranging the brands for the carousel
    brands = Brand.objects.all()
    quant_brands = len(brands)
    
    first_slide_carousel = []
    second_slide_carousel = []
    third_slide_carousel = []
    fourth_slide_carousel = []
    
    count = 1
    for brand in brands:
        if count <= 4:
            first_slide_carousel.append(brand)
        elif count >= 5 and count <= 8:
            second_slide_carousel.append(brand)
        elif count >= 9 and count <= 12:
            third_slide_carousel.append(brand)
        elif count >= 13 and count <= 16:
            fourth_slide_carousel.append(brand)
        count += 1
    
    context = {
        'cart_quantity': cart_quantity,
        'categories': categories,
        'quant_brands': quant_brands,
        'first_slide_carousel': first_slide_carousel,
        'second_slide_carousel': second_slide_carousel,
        'third_slide_carousel': third_slide_carousel,
        'fourth_slide_carousel': fourth_slide_carousel,
    }
    return render(request, 'index.html', context)

def about(request):
    cart_quantity = quantity_of_items(request)
    categories = Category.objects.all()
    
    # Arranging the brands for the carousel
    brands = Brand.objects.all()
    quant_brands = len(brands)
    
    first_slide_carousel = []
    second_slide_carousel = []
    third_slide_carousel = []
    fourth_slide_carousel = []
    
    count = 1
    for brand in brands:
        if count <= 4:
            first_slide_carousel.append(brand)
        elif count >= 5 and count <= 8:
            second_slide_carousel.append(brand)
        elif count >= 9 and count <= 12:
            third_slide_carousel.append(brand)
        elif count >= 13 and count <= 16:
            fourth_slide_carousel.append(brand)
        count += 1
    
    context = {
        'cart_quantity': cart_quantity,
        'categories': categories,
        'quant_brands': quant_brands,
        'first_slide_carousel': first_slide_carousel,
        'second_slide_carousel': second_slide_carousel,
        'third_slide_carousel': third_slide_carousel,
        'fourth_slide_carousel': third_slide_carousel,
    }
    return render(request, 'about.html', context)

def products(request):
    cart_quantity = quantity_of_items(request)
    products = Product.objects.all()
    categories = Category.objects.all()
            
    # Arranging the brands for the carousel
    brands = Brand.objects.all()
    quant_brands = len(brands)
    
    first_slide_carousel = []
    second_slide_carousel = []
    third_slide_carousel = []
    fourth_slide_carousel = []
    
    count = 1
    for brand in brands:
        if count <= 4:
            first_slide_carousel.append(brand)
        elif count >= 5 and count <= 8:
            second_slide_carousel.append(brand)
        elif count >= 9 and count <= 12:
            third_slide_carousel.append(brand)
        elif count >= 13 and count <= 16:
            fourth_slide_carousel.append(brand)
        count += 1
    
    # Pagination
    paginator = Paginator(products, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    products = page_obj
    
    context = {
        'products': products,
        'categories': categories,
        'cart_quantity': cart_quantity,
        'brands': brands,
        'quant_brands': quant_brands,
        'first_slide_carousel': first_slide_carousel,
        'second_slide_carousel': second_slide_carousel,
        'third_slide_carousel': third_slide_carousel,
        'fourth_slide_carousel': fourth_slide_carousel,
        'page_obj': page_obj,
    }
    return render(request, 'shop.html', context)

def contact(request):
    cart_quantity = quantity_of_items(request)
    categories = Category.objects.all()
    
    context = {
        'cart_quantity': cart_quantity,
        'categories': categories,
    }
    return render(request, 'contact.html', context)

def search(request):
    cart_quantity = quantity_of_items(request)
    categories = Category.objects.all()
    
    if request.method == 'GET':
        search_term = request.GET.get('term')
        
        if search_term != None:
            if search_term == '':
                product_search = ''
            else:
                product_search = Product.objects.filter(Q(title__icontains=search_term) | Q(color__icontains=search_term))
        else:
            product_search = ''
            
    context = {
        'cart_quantity': cart_quantity,
        'categories': categories,
        'product_search': product_search,
    }
    return render(request, 'search.html', context)

def category_products(request, pk):
    categories = Category.objects.all()
    cart_quantity = quantity_of_items(request)
    
    brands = Brand.objects.all()
    filtered_products = Product.objects.filter(category=pk)
            
    # Arranging the brands for the carousel
    brands = Brand.objects.all()
    quant_brands = len(brands)
    
    first_slide_carousel = []
    second_slide_carousel = []
    third_slide_carousel = []
    fourth_slide_carousel = []
    
    count = 1
    for brand in brands:
        if count <= 4:
            first_slide_carousel.append(brand)
        elif count >= 5 and count <= 8:
            second_slide_carousel.append(brand)
        elif count >= 9 and count <= 12:
            third_slide_carousel.append(brand)
        elif count >= 13 and count <= 16:
            fourth_slide_carousel.append(brand)
        count += 1

    # Pagination
    paginator = Paginator(filtered_products, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    products = page_obj

    context = {
        'products': products,
        'categories': categories,
        'cart_quantity': cart_quantity,
        'brands': brands,
        'quant_brands': quant_brands,
        'first_slide_carousel': first_slide_carousel,
        'second_slide_carousel': second_slide_carousel,
        'third_slide_carousel': third_slide_carousel,
        'fourth_slide_carousel': fourth_slide_carousel,
        'page_obj': page_obj,
    }
    return render(request, 'shop.html', context)

def brand_products(request, pk):
    cart_quantity = quantity_of_items(request)
    categories = Category.objects.all()
    
    brands = Brand.objects.all()
    filtered_products = Product.objects.filter(brand=pk)
            
    # Arranging the brands for the carousel
    brands = Brand.objects.all()
    quant_brands = len(brands)
    
    first_slide_carousel = []
    second_slide_carousel = []
    third_slide_carousel = []
    fourth_slide_carousel = []
    
    count = 1
    for brand in brands:
        if count <= 4:
            first_slide_carousel.append(brand)
        elif count >= 5 and count <= 8:
            second_slide_carousel.append(brand)
        elif count >= 9 and count <= 12:
            third_slide_carousel.append(brand)
        elif count >= 13 and count <= 16:
            fourth_slide_carousel.append(brand)
        count += 1
    
    # Pagination
    paginator = Paginator(filtered_products, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    products = page_obj

    context = {
        'products': products,
        'categories': categories,
        'cart_quantity': cart_quantity,
        'brands': brands,
        'quant_brands': quant_brands,
        'first_slide_carousel': first_slide_carousel,
        'second_slide_carousel': second_slide_carousel,
        'third_slide_carousel': third_slide_carousel,
        'fourth_slide_carousel': fourth_slide_carousel,
        'page_obj': page_obj,
    }
    return render(request, 'shop.html', context)

def single_product(request, slug):
    cart_quantity = quantity_of_items(request)
    categories = Category.objects.all()
    
    product = Product.objects.get(slug=slug)
    related_products = Product.objects.filter(category=product.category, gender=product.gender).exclude(slug=slug)[:16]
    
    # Arranging the images for the carousel
    secondary_images = ProductImage.objects.filter(product=product)
    quant_images = len(secondary_images) + 1
    
    first_slide_carousel = []
    second_slide_carousel = []
    count = 2
    for image in secondary_images:
        if count <= 3:
            first_slide_carousel.append(image)
        elif count > 3 and count <= 6:
            second_slide_carousel.append(image)
        count += 1

    context = {
        'product': product,
        'categories': categories,
        'quant_images': quant_images,
        'first_slide_carousel': first_slide_carousel,
        'second_slide_carousel': second_slide_carousel,
        'related_products': related_products,
        'cart_quantity': cart_quantity
    }
    return render(request, 'shop-single.html', context)

@login_required(redirect_field_name='login')
def cart(request):
    cart_quantity = quantity_of_items(request)
    categories = Category.objects.all()
    
    order_product = OrderProduct.objects.filter(user=request.user)

    amount = 0
    for product in order_product:
        if product.product.discount_price:
            amount += (product.product.discount_price * product.quantity)
        else:
            amount += (product.product.price * product.quantity)
        
    round_amount = round(amount, 2)
        
    context = {
        'orders': order_product,
        'categories': categories,
        'amount': round_amount,
        'cart_quantity': cart_quantity,
    }
    return render(request, 'cart.html', context)

@login_required(redirect_field_name='login')
def ad_to_cart(request, slug):
    product = Product.objects.get(slug=slug)
    order_product = OrderProduct.objects.filter(user=request.user, product=product)
    
    if order_product:
        new_quantity = OrderProduct.objects.get(user=request.user, product=product).quantity
        new_quantity += 1
        
        OrderProduct.objects.filter(user=request.user, product=product).update(quantity=new_quantity)
    else:
        OrderProduct.objects.create(user=request.user, product=product)
    
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(redirect_field_name='login')
def del_to_cart(request, slug):
    product = Product.objects.get(slug=slug)
    order_product = OrderProduct.objects.filter(user=request.user)
    
    for prod in order_product:
        if prod.product.slug == slug:
            if prod.quantity > 1:
                quantity = OrderProduct.objects.get(user=request.user, product=product).quantity
                quantity -= 1
                OrderProduct.objects.filter(user=request.user, product=product).update(quantity=quantity)
            else:
                prod.delete()
    
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(redirect_field_name='login')
def purchase(request):
    cart_quantity = quantity_of_items(request)
    categories = Category.objects.all()
    
    order_product = OrderProduct.objects.filter(user=request.user)
    for prod in order_product:
        product = Product.objects.get(slug=prod.product.slug)
        quantity = product.quantity - prod.quantity
        Product.objects.filter(slug=prod.product.slug).update(quantity=quantity)
        OrderProduct.delete(prod)

    context = {
        'cart_quantity': cart_quantity,
        'categories': categories,
    }
    return render(request, 'purchase.html', context)

@login_required(redirect_field_name='login')
def favorite(request):
    cart_quantity = quantity_of_items(request)
    categories = Category.objects.all()
    
    favorite_product = FavoriteProduct.objects.filter(user=request.user)
    favorite_quantity = len(FavoriteProduct.objects.filter(user=request.user))
    
    context = {
        'favorites': favorite_product,
        'favorite_quantity': favorite_quantity,
        'cart_quantity': cart_quantity,
        'categories': categories,
    }
    return render(request, 'favorite.html', context)

@login_required(redirect_field_name='login')
def ad_to_favorite(request, slug):
    product = Product.objects.get(slug=slug)
    
    if not FavoriteProduct.objects.filter(user=request.user, product=product):
        FavoriteProduct.objects.create(user=request.user, product=product)
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(redirect_field_name='login')
def del_to_favorite(request, slug):
    favorite_product = FavoriteProduct.objects.filter(user=request.user)
    for product in favorite_product:
        if product.product.slug == slug:
            product.delete()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(redirect_field_name='login')
def profile(request):
    cart_quantity = quantity_of_items(request)
    categories = Category.objects.all()
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        if first_name != request.user.first_name:
            User.objects.filter(username=request.user.username).update(first_name=first_name)
    
        if last_name != request.user.last_name:
            User.objects.filter(username=request.user.username).update(last_name=last_name) 
            
        if (email != request.user.email):
            if User.objects.filter(email=email):
                messages.info(request, 'Esse email já existe!')
            else:
                User.objects.filter(username=request.user.username).update(email=email)
        
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        new_password2 = request.POST.get('new_password2')
        if old_password != '' or new_password != '' or new_password2 != '':
            if auth.authenticate(username=request.user.username, password=old_password):
                if new_password == new_password2:
                    user = User.objects.get(username=request.user.username)
                    user.set_password(new_password)
                    user.save()
                else:
                    messages.info(request, 'As novas senhas precisam ser iguais.')
            else:
                messages.info(request, 'A senha antiga está incorreta.')
        
        return redirect(request.META.get('HTTP_REFERER'))
    
    context = {
        'cart_quantity': cart_quantity,
        'categories': categories,
    }
    return render(request, 'profile.html', context=context)

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
  
        user_auth = auth.authenticate(username=username, password=password)
        if user_auth:
            auth.login(request, user_auth)
            return redirect('index')
        else:
            messages.info(request, 'Usuário ou Senha incorretos.')
            return redirect('login')
        
    return render(request, 'login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'O usuário já existe!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'O email já existe!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'As senhas não são iguais!')
            return redirect('register')
        
    return render(request, 'register.html')

@login_required(redirect_field_name='index')
def logout(request):
    auth.logout(request)
    return redirect('index')