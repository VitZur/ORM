import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
           reader = csv.DictReader(file)
           for row in reader:
               phone = Phone(
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],  
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists'] == 'True',
                    slug=slugify(row['name'])  
                )
               phone.save()
        self.stdout.write(self.style.SUCCESS('Данные успешно импортированны'))