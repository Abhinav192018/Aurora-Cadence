from django.urls import path
from app import views

urlpatterns = [

    path('', views.index, name='home'),
    path('products/', views.Products, name='products'),
    path('product/details/',views.Product_details,name="product_details"),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('about/', views.about, name='about'),
    path('gallery/', views.Gallery, name='gallery'),
    path('contact/',views.contact,name="contact"),
    path("cart/",views.cart, name="cart"),


    # categories-----------------------------

    path('gold-plated/', views.gold_plated_view, name='gold_plated'),
    path('swarovski/', views.swarovski_view, name='swarovski'),
    path('celebrity/', views.celebrity_view, name='celebrity'),
    path('necklace/', views.necklace_view, name='necklace'),
    path('bangles/', views.bangles_view, name='bangles'),
    path('bracelets/', views.bracelets_view, name='bracelets'),
    path('earrings/', views.earrings_view, name='earrings'),
    path('anklets/', views.anklets_view, name='anklets'),
    path('rings/', views.rings_view, name='rings'),
]