from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from .models import Product, CartItem


def home(request):
    """Home page with welcome message based on authentication status."""
    # Get featured products for homepage
    featured_products = Product.objects.all()[:6]
    paginator = Paginator(featured_products, 6)
    page_obj = paginator.get_page(1)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'shop/home.html', context)


def products(request):
    """Products page with grid layout, search, and pagination."""
    products_list = Product.objects.all().order_by('-created_at')
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        products_list = products_list.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(products_list, 9)  # Show 9 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'shop/products.html', context)


@login_required
def cart(request):
    """Cart page showing items and calculating total price."""
    cart_items = CartItem.objects.filter(user=request.user)
    
    # Calculate total price dynamically
    total_price = sum(item.total_price for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'shop/cart.html', context)


@login_required
def add_to_cart(request, product_id):
    """Add product to cart."""
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('products')


@login_required
def remove_from_cart(request, cart_item_id):
    """Remove item from cart."""
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')


def product_detail(request, product_id):
    """Product detail page with image gallery."""
    product = get_object_or_404(Product, id=product_id)
    # Get suggested products (exclude current product)
    suggested_products = Product.objects.exclude(id=product_id)[:4]
    
    context = {
        'product': product,
        'suggested_products': suggested_products,
    }
    return render(request, 'shop/product_detail.html', context)


@login_required
def profile(request):
    """User profile page."""
    context = {}
    return render(request, 'shop/profile.html', context)


def signup(request):
    """User registration/signup view."""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after signup
            login(request, user)
            messages.success(request, f'Welcome to ShopSmart, {user.username}! Your account has been created successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'shop/signup.html', {'form': form})


def logout_view(request):
    """Custom logout view that redirects to login page."""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

