from django.shortcuts import render, get_object_or_404
from .models import Book
from datetime import datetime, timedelta


def book_list (request):
    books = Book.objects.all().order_by('pub_date')
    return render(request, 'book/book_list.html' , {'book':books})

def boook_by_data(request, pub_date):
    try:
        pub_date_obj = datetime.strftime(pub_date,'%Y-%m-%d').date()
    except ValueError:
        pub_date_obj = None

    if pub_date_obj is None:
        return render(request, '404-html', status=400)
    
    books = Book.objects.filter(pub_date=pub_date_obj)

    previos_book = Book.objects.filter(pub_date__lt=pub_date_obj).order_by('-pub_date').first()
    next_book = Book.objects.filter(pub_date_gt=pub_date_obj).order_by('pub_date').first()

    context = {
        'book': books,
        'previos_book': previos_book,
        'next_book': next_book,
        'pub_date': pub_date_obj
    }

    return render(request, 'book/book_by_date.html', context)