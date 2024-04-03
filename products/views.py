from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, inccluding sorting and search queries """

    prodcuts = Product.objects.all()

    context = {
        'products': prodcuts,
    }

    return render(request, 'products/products.html', context)
