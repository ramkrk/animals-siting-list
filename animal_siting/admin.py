"""
Admin for animal siting
"""

# Core Imports
from django.contrib import admin

# Local Imports
from .models import Animal, Breed, SitingList


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    """ Animal Model Registration to admin site """
    model = Animal
    filter_horizontal = ("breeds",)
    list_display = ('name', 'breed_name')


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    """ Breed Model Registration to admin site """
    model = Breed
    search_fields = ('name',)
    list_display = ('name',)


@admin.register(SitingList)
class SitingListAdmin(admin.ModelAdmin):
    """ Siting Model Registration to admin site """
    model = SitingList
    list_display = ('animal_name', 'breed_name', 'created')
