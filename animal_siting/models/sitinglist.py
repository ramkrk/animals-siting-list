"""
 Modal: Siting List
 ForeignKey: Breed
 Info: Holds siting list of animal's breed information
"""

# Django Import
from django.db import models

# Local Import
from .breeds import Breed


class SitingList(models.Model):
    """Breed Siting List Data"""

    class Meta:
        verbose_name = 'Siting Info'
        verbose_name_plural = 'Siting List'

    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    created = models.DateField()

    def __str__(self):
        return self.breed.name

    def animal_name(self):
        animal = self.breed.animals.all()[0].name
        return f"{animal}"

    def breed_name(self):
        return f"{self.breed.name}"
