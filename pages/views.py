from django.shortcuts import render
from Products.models import Product

# Create your views here.
def home(request):
    # Fetching all products that are marked available & display only 8 per page
    products = Product.objects.filter(available=True).order_by('-created')[:8]
    context = {
        'products':products
    }
    return render(request,'pages/home.html',context)