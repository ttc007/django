from django.shortcuts import render, redirect
from products.models import Product, Category, Industry
from character.models import Character
from django.http import JsonResponse, HttpResponse
from datetime import datetime
import array
from django.utils.translation import ugettext as _
from django.contrib import auth
from django.contrib.auth.models import User
from character.models import Vault
from django.utils import translation
from django.shortcuts import get_object_or_404


def index(request):
    output = _("Welcome to my site.")
    industrys = Industry.objects.all()
    products = Product.objects.all()
    categorys = Category.objects.all()
    if request.user.is_active :
        print(request.user.password)
        try:
            character = Character.objects.get(user_id=request.user.id)
        except Character.DoesNotExist:
            character = None
            return render(request, 'character/createCharacter.html')
    else:
        return redirect('/account/login_view')
    # message =  _('Today is %(month)s %(day)s.') % {'month': '3', 'day': '4'}
    context = {'products' : products,
               'categorys' : categorys,
               'character':character,
               # 'message': message
               }
    return render(request, 'index.html', context)

def shop(request):
    output = _("Welcome to my site.")
    industrys = Industry.objects.all()
    products = Product.objects.all()
    categorys = Category.objects.all()
    if request.user.is_active :
        character = Character.objects.get(user_id=request.user.id)
    else:
        return redirect('/account/login_view')
    context = {'products' : products,
               'categorys' : categorys,
               'character':character,}
    return render(request, 'shop/shop.html', context)


def create(request):
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    return render(request, 'products/create.html', context)

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
    return render(request, 'products/edit.html', context)

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

def buy(request, id):
    character = Character.objects.get(user_id=request.user.id)
    product = Product.objects.get(id=id)
    if character.gold > product.price:
        character.gold = character.gold - product.price
        vault = Vault(character_id=character.id, item=id)
        character.save()
        vault.save()

    return redirect('/')



def ajaxCategory(request):
    products = Product.objects.filter(category_id = request.GET['id'])
    data = {'product':[]}
    for product in products:
        data['product'].append({'id': request.GET['id'], 'name' : product.name})
    response = JsonResponse(data)
    return response
