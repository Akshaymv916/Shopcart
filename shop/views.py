import json
from telnetlib import LOGOUT
from typing import Self
from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from . models import *
from django.contrib import messages
from shop.form import CustomeUserForm
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q


# Create your views here.
def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products":products})


def logout_page(request):
    if request.user.is_authenticated:
      logout(request)
      messages.success(request,"logged out successfully")
    return redirect('/')
      

def login_page(request):
    if request.user.is_authenticated:
       return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Login Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect('/login')    
        return render(request,"shop/login.html")


def register(request):
    form=CustomeUserForm()
    if request.method=='POST':
        form=CustomeUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You Can Login Now")
            return redirect('/login')
    return render(request,"shop/register.html",{"form":form})


def collection(request):
    catagory=Category.objects.filter(status=0)
    return render(request,"shop/collections.html",{"category":catagory})


def collectionview(request,name):
    if(Category.objects.filter(status=0)):
        products=Product.objects.filter(category__name=name)
        return render(request,"shop/products/index.html",{"products":products,"category_name":name})     
    else:
        messages.warning(request,"No such Category Found")
        return redirect('collections')
    
    
def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            Products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/product_details.html",{"prodcuts":Products})

        else:
            messages.error(request,"No such Product Found")
            return redirect("collection")
    else:
         messages.error(request,"No such Category Found")
         return redirect("collection")


def addtocart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
     if request.user.is_authenticated:
        data=json.load(request)
        product_qty=data['product_qty']
        product_id=data['pid']
        #print(request.user.id)
        admin.site.register(Customer)

        return JsonResponse({'status':'Product Already in Cart'}, status=200)
     else:
        if product_status.quantity>=product_qty:
            Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
            return JsonResponse({'status':'Product Added to Cart'}, status=200)
        else:
            return JsonResponse({'status':'Product Stock Not Available'}, status=200)
    
def cart_page(request):
   if request.user.is_authenticated:
      cart=Cart.objects.filter(user=request.user)
      return render(request,"shop/cart.html",{"cart":cart})
   else:
      messages.info(request,"Please Login")
      return redirect("/")
   

def remove_cart(request,cid):
   cartitem=Cart.objects.filter(id=cid)
   cartitem.delete()
   return redirect("/cart")


def checkout(request):
   if request.user.is_authenticated:
      messages.success(request,"Thank You,Your Item Purchase Successfully")
      return redirect("/")
   else:
      return redirect("/cart")
      

def low(request):
   data=Product.objects.all().order_by('selling_price')
   return render(request,"shop/sort.html",{'data':data})


def high(request):
   data=Product.objects.all().order_by('-selling_price')
   return render(request,"shop/sort.html",{'data':data})

def search(request):
   searchterm=""
   if 'search' in request.GET:
      searchterm=request.GET['search']
      products=Product.objects.all().filter(name__icontains=searchterm)
   return render(request,"shop/search.html",{'products':products,'searchterm':searchterm})