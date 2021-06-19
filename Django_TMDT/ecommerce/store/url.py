from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.update_item, name="update_item"),
    path('delete_item/', views.delete_item, name="delete_item"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('update_cart/', views.update_cart, name="update_cart"),
    path('ship/', views.fill_ship, name="ship"),
    path('search/', views.search, name="search"),
]
