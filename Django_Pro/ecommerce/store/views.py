import json

from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print("oke1")
        if form.is_valid():
            print("oke2")
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')

    context = {'form': form}
    return render(request, 'store/accounts/register.html', context)


def loginPage(request):
    system_messages = messages.get_messages(request)
    for message in system_messages:
        # This iteration is necessary
        pass
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
        else:
            messages.info(request, 'Sai dang nhap')
    context = {}
    return render(request, 'store/accounts/login.html', context)

def logoutUser(request):
    logout(request);
    return redirect('login')


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store1.html', context)


@login_required(login_url="/login/")
def cart(request):
    # if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer)
    items = order.orderitem_set.all()
    # else:
    #     items = []
    #     order = {'get_cart_total': 0, }

    context = {'items': items, 'orders': order}
    return render(request, 'store/cart2.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def update_item(request):
    print("alo")
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Id:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    print("oke chưa")
    return JsonResponse('Item is add', safe=False)

def delete_item(request):
    print("alo")
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Id:', productId)

    customer = request.user.customer
    print("nme")
    order, created = Order.objects.get_or_create(customer=customer)
    orderItem, created = OrderItem.objects.get_or_create(order=order, id=productId)
    if action == "delete":
        orderItem.delete()
    print("oke chưa")
    return JsonResponse('Item is add', safe=False)



def update_cart(request):
    print("alo")
    data = json.loads(request.body)
    productId = data['productId']
    quant = data['quantity']
    print('quantity:', quant)
    print('Id:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order = Order.objects.get(customer=customer)
    orderItem = OrderItem.objects.get(order=order, product=product)
    orderItem.quantity = quant
    orderItem.save()
    print("oke nhe")
    return JsonResponse('Item is add', safe=False)

def fill_ship(request):
    cotext = {}
    return render(request, 'store/shipment.html', cotext)

def search(request):
    q = request.GET['q']
    data = Product.objects.filter(name__contains=q).order_by('id')
    return render(request, 'store/store1.html', {'products': data})