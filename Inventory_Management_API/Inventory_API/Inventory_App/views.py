from django.shortcuts import render, redirect
from .forms import ProductForm, RegisterForm, UpdateForm
from .models import Product
from django.contrib.auth import authenticate, login, logout
# The login_required decorator to protect views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from rest_framework import filters, generics
from .serializers import ProductSerializer

# Create your views here.

# Register View
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'Inventory_App/register.html', {'form':form})

# Login View
def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials"
    return render(request, 'Inventory_App/login.html', {'error':error_message})

# Logout View
def logout_view(request):
    #if request.method == 'POST':
        logout(request)
        return redirect('login')
    #else:
        #return redirect('logout')
    
#Users View
def users_view(request):
    users = User.objects.all()
    return render(request, 'Inventory_App/user_list.html', {'users': users})

# Profile View
def profile_view(request):
    user = request.user
    return render(request, 'Inventory_App/profile.html', {'user': user})

# User Update View
def user_update_view(request, username):
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            #password = form.cleaned_data.get("password")
            #user_name = request.user.username
            #user = User.objects.filter(username=user_name).update(username=username, email=email, password=password)
            
            user = form.save()
            user.username = username
            user.email = email
            #user.password = password
            user.save()
            #user.objects.update(username=username, email=email, password=password)
            return redirect('profile')
    else:
        form = UpdateForm()
    return render(request, 'Inventory_App/profile_update.html', {'form':form})

# Profile Delete View
def profile_delete_view(request, username):
    user = User.objects.get(username=username)
    form = RegisterForm()
    if request.method == "POST":
        user.delete()
        return redirect('login')
    return render(request, 'Inventory_App/profile_delete_confirm.html')

# User Delete View
def user_delete_view(request, username):
    user = User.objects.get(username=username)
    form = RegisterForm()
    if request.method == "POST":
        user.delete()
        return redirect('user_list')
    return render(request, 'Inventory_App/user_delete_confirm.html')

# Home View
# Using the decorator
@login_required
def home_view(request):
    return render(request, 'Inventory_App/home.html')

# Create View
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            added_product = form.save()
            added_product.added_by = request.user
            added_product.save()
            return redirect('product_list')
    return render(request, 'Inventory_App/product_form.html', {'form': form})

#All Product View
def all_product_list_view(request):
    product_list = Product.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'price', 'quantity']
    return render(request, 'Inventory_App/all_product_list.html', {'product_list': product_list})

# Read View
def product_list_view(request):
    product_list = Product.objects.filter(added_by=request.user) or Product.objects.filter(updated_by=request.user)
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'price', 'quantity']
    return render(request, 'Inventory_App/product_list.html', {'product_list': product_list})

# Read Class Based View
class product_list_class_view(generics.ListAPIView):
    #queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'price', 'quantity']
    def get_queryset(self):
        return Product.objects.filter(added_by=self.request.user) or Product.objects.filter(updated_by=self.request.user)
    #def view_product_list(self, request):  
        #product_list = self.queryset.objects.filter(added_by=request.user) or Product.objects.filter(updated_by=request.user)
        #return render(request, 'Inventory_App/product_list.html', {'product_list': product_list})

# Update View
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            updated_product = form.save()
            updated_product.updated_by = request.user
            updated_product.save()
            return redirect('product_list')
    return render(request, 'Inventory_App/product_form.html', {'form': form})

# Delete View
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm()
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'Inventory_App/product_delete_confirm.html', {'product': product})