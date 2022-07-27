"""
 Modal: Breed
 ForeignKey: Animal
 Info: Holds animal's breed information
"""

import datetime
from django.db import models


class Breed(models.Model):
    """Breed Data"""
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Breed'
        verbose_name_plural = 'Breeds'

    @property
    def animal_name(self):
        return self.animals.name

