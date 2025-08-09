from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import supportForm, add_product
from .models import Products


def index(request):
    products = Products.objects.all()
    
    return render(request, 'shop/index.html', {
            "products" : products, 
            'caller_view' : 'home'
            })

def Add_products_view(request):
    product_form = add_product()
    if request.method == 'POST':
        product_form = add_product(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('add_product_page')
        else:
            print("Invalid", product_form.cleaned_data)
            
    return render(request, 'shop/add_product.html', {
            'product_form' : product_form,
            'caller_view' : 'add_prodect'
            })

def product_details_view(request, slug):
    products = get_object_or_404(Products, slug=slug)
    
    return render(request, 'shop/product-details.html', {
            'product': products, 
            'caller_view' : 'details'
            })

def support(request):
    form = supportForm()
    if request.method == 'POST':
        form = supportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('support_page')
        else:
            print("Invalid", form.cleaned_data)
    return render(request, 'shop/support_page.html', {
           'form' : form, 
           'caller_view' : 'support'
           })

