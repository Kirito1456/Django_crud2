from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreate
from django.http import HttpResponse
# Create your views here.

# READ
def index(request):
    inventory = Product.objects.all()
    return render(request, 'product/index.html', {'inventory':inventory})

# CREATE
def add(request):
    """
        This function adds item in the database
        Accepts a POST request
        If form submitted is valid, it saves the item in the database and redirect to initial home view
    """
    upload = ProductCreate()
    if request.method == 'POST':
        upload = ProductCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("your form is wrong, reload")
    else:
        return render(request, 'product/index.html', {'upload_form':upload})

# UPDATE
def update_product(request, product_id):
    product_id = int(product_id)
    try:
        product_sel = Product.objects.get(id = product_id)
    except Product.DoesNotExist:
        return redirect('index')
    product_form = ProductCreate(request.POST or None, instance=product_sel)
    if product_form.is_valid():    
        product_form.save()
        return redirect('index')
    return render(request, 'product/index.html', {'upload_form':product_form})

# DELETE
def delete_product(request, product_id):
    product_id = int(product_id)
    try:
        product_sel = Product.objects.get(id = product_id)
    except Product.DoesNotExist:
        return redirect('index')
    product_sel.delete()
    return redirect('index')