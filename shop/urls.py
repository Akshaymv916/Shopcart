from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('collections/',views.collection,name="collection"),
    path('collections/<str:name>',views.collectionview,name="collections"),
    path('collections/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('addtocart',views.addtocart,name="addtocart"),
    path('cart',views.cart_page,name="cart"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('checkout',views.checkout,name="checkout"),
    path('low',views.low,name="low"),
    path('high',views.high,name="high"),
    path('search',views.search,name="search")


]
