from django.shortcuts import render,get_object_or_404
from .models import Cake,Order

# Create your views here.

def home(request):
   return render(request, 'index.html')


def my_view(request):
    context = {
        'css_file': 'myapp/style.css',
        'js_file': 'myapp/script.js',
    }
    return render(request, 'index.html', context)


def cake_list(request):
    cakes = Cake.objects.all()
    return render(request, 'home/cake_list.html', {'cakes':cakes})

def cake_detail(request,id):
    cake = get_object_or_404(Cake, id=id)
    return render(request, 'home/cake_detail.html', {'cake':cake})

def place_order(request):
    return render(request, 'home/place_order.html')

def order_confirmation(request):
    order = get_object_or_404(Order, id=id)
    return render(request, 'home/order_confirmation.html', {'order':order})