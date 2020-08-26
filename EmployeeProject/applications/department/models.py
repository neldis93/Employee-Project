from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField('Name',max_length=40, unique=True)
    short_name = models.CharField('Short Name', max_length=30) # blank=True es para que el campo sea solo opcional o no obligatorio
    anulate = models.BooleanField('Anulate', default= False)

    class Meta:
        #verbose_name= 'My Department'
        #verbose_name_plural= 'Area of the company'
        ordering= ['name']
        #unique_together= ('name','short_name')

    def __str__(self):
        return  '-' + self.short_name