from django.shortcuts import render, redirect
from products.models import Product, Category, Industry
from character.models import Character
from django.http import JsonResponse, HttpResponse
from datetime import datetime
import array
from pprint import pprint
from django.utils.translation import ugettext as _

def index(request):
    output = _("Welcome to my site.")
    industrys = Industry.objects.all()
    products = Product.objects.all()
    categorys = Category.objects.all()
    character = Character.objects.get(id=1)
    context = {'products' : products,
               'categorys' : categorys,
               'character':character}
    return render(request, 'index.html', context)


def create(request):
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    return render(request, 'create.html', context)

def store(request):
    print "DEBUG image ", (request.POST)
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
    categorys = Category.objects.all()
    context = {'product': product,
               'categorys': categorys}
    return render(request, 'edit.html', context)

def update(request, id):
    product = Product.objects.get(id = id)
    product.name = request.POST['name']
    product.category_id = request.POST['category_id']
    product.create_at = datetime.today()
    print "DEBUG image ", (request.POST)
    if request.FILES.get('image'):
        image = request.FILES['image']
        image.name = request.POST['name'] + ".png"
        product.image = image
    product.save()
    return redirect('/')

def ajaxCategory(request):
    products = Product.objects.filter(category_id = request.GET['id'])
    data = {'product':[]}
    for product in products:
        data['product'].append({'id': request.GET['id'], 'name' : product.name})
    response = JsonResponse(data)
    return response
