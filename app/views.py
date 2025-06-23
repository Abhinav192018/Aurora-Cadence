from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main_page/index.html')

def Products(request):
    return render(request, 'main_page/products.html')

def my_orders(request):
    return render(request, 'main_page/my_orders.html')

def about(request):
    return render(request, 'main_page/about.html')

def Gallery(request):
    return render(request, 'main_page/gallery.html')