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

def contact(request):
    return render(request,'main_page/condact.html')

def Product_details(request):
    return render(request,'main_page/product_details.html')

def cart(request):
    return render(request,'main_page/cart.html')
# ---------------------------------------------------------------------------


def gold_plated_view(request):
    return render(request, 'categories/gold_plated.html')

def swarovski_view(request):
    return render(request, 'categories/swarovski.html')

def celebrity_view(request):
    return render(request, 'categories/celebrity.html')

def necklace_view(request):
    return render(request, 'categories/necklace.html')

def bangles_view(request):
    return render(request, 'categories/bangles.html')

def bracelets_view(request):
    return render(request, 'categories/bracelets.html')

def earrings_view(request):
    return render(request, 'categories/earrings.html')

def anklets_view(request):
    return render(request, 'categories/anklets.html')

def rings_view(request):
    return render(request, 'categories/rings.html')


