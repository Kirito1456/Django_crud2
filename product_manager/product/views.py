from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreate
from django.http import HttpResponse

# Create your views here.

# READ
def index(request):
    """
        This function loads the initial view
        Also shows product information from the database
    """ 
    
    upload = ProductCreate()
    edits = []
    for product in Product.objects.all():
        product_sel = Product.objects.get(id = product.id)
        edits.append({
            "form": ProductCreate(request.POST or None, instance=product_sel),
            "product": product_sel
        })
    context = {
        "form": upload,
        "inventory": Product.objects.all(),
        "edits": edits
    }
    return render(request, 'product/index.html', context)

# CREATE
def add(request):
    """
        Adds product in the database
        If form submitted is valid, it saves the product in the database and redirect to initial home view
    """
    upload = ProductCreate()
    if request.method == 'POST':
        upload = ProductCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('product:index')
        else:
            return HttpResponse("your form is wrong, reload")
    else:
        return redirect('product:index')

# UPDATE
def update_product(request, product_id):
    """
        Updates product in the database
        If form submitted is valid, it saves the product in the database and redirect to initial home view
    """
    product_id = int(product_id)
    try:
        product_sel = Product.objects.get(id = product_id)
    except Product.DoesNotExist:
        return redirect('product:index')
    product_form = ProductCreate(request.POST or None, instance=product_sel)
    if product_form.is_valid():    
        product_form.save()
        return redirect('product:index')
    else:
        return HttpResponse("your form is wrong, reload")

# DELETE
def delete_product(request, product_id):
    """
        Delete product in the database
    """
    product_id = int(product_id)
    try:
        product_sel = Product.objects.get(id = product_id)
    except Product.DoesNotExist:
        return redirect('product:index')
    product_sel.delete()
    return redirect('product:index')