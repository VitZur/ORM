from django.contrib import admin

from books.models import Book

admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'pub_date',)


admin.site.register(Book, BookAdmin)
