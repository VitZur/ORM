from django.shortcuts import render
from .models import Phone

def show_product(request):
   
    sort_by = request.GET.get('sort', 'name')  

    sort_options = {
        'name':'name',
        'price':'price',
        'price_desc':'-price'
    }

    phones = Phone.objects.all().order_by(sort_options.get(sort_by,'name'))
    
    return render(request, 'catalog.html', {'phones':phones})

def index(request):
    return render(request, 'phones/index.html')

