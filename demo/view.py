from django.shortcuts import render, redirect
from products.models import Product
from datetime import datetime

def index(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'index.html', context)


def create(request):
    return render(request, 'create.html')

def store(request):
    if request.FILES.get('image'):
        image = request.FILES['image']
        image.name = request.POST['name'] + ".png"
    else:
        image = "default.jpg"
    product = Product(name = request.POST['name'],
                      category_id = request.POST['category_id'],
                      create_at = datetime.today(),
                      image = image)
    product.save()
    return redirect('/')

def delete(request, id):
    product = Product.objects.get(id = id)
    product.delete()
    return redirect('/')

def edit(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render(request, 'edit.html', context)

def update(request, id):
    product = Product.objects.get(id=id)
    product.name = request.POST['name']
    product.category_id = request.POST['category_id']
    product.create_at="2017-12-11"
    product.save()
    return redirect('/')