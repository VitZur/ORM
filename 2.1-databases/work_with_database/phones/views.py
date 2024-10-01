from django.shortcuts import render
from .models import Phone

def show_product(request):
   
    sort_by = request.GET.get('sort', 'name')  

    if sort_by == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort_by == 'price':
        phones = Phone.objects.all().order_by('price')
    elif sort_by == 'price_desc':
        phones = Phone. objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()
        
    return render(request, 'catalog.html', {'phones':phones})

def index(request):
    return render(request, 'phones/index.html')

