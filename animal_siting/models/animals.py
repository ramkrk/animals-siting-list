"""
 Modal: Animal
 Info: Holds animal information
"""
# Django Import
from django.db import models

# Local Import
from .breeds import Breed


class Animal(models.Model):
    """Animal Data"""
    name = models.CharField(max_length=30)
    breeds = models.ManyToManyField(Breed, verbose_name='list of breeds', related_name="animals")

    def __str__(self):
        return self.name

    def breed_name(self):
        breeds_list = ", ".join([breed.name for breed in self.breeds.all()])
        return f'{breeds_list}'

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'
