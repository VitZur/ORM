from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to='phones/')
    release_date = models.DateTimeField()
    ite_exits = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug == slugify(self.name)
        super(Phone, self).save(*args,**kwargs)

    def __str__(self):
        return self.name