# Python Import
import datetime

# Django Import
from django.test import TestCase


# Create your tests here.
from .models import Animal, Breed, SitingList
from .views import get_siting_details, save_siting_list


class SitingListTest(TestCase):
    """ Test for sitting controllers """
    def setUp(self):
        breed = Breed.objects.create(name="Labrador")
        animal = Animal.objects.create(name="Dog")
        animal.breeds.add(breed)
        SitingList.objects.create(id=1, breed=breed, created=datetime.datetime.today())

    def test_get_siting_details(self):
        slist = SitingList.objects.all()
        siting_list = get_siting_details()
        expected_list = [{'animal': sl.breed.animals.all()[0].name,
             'breed': sl.breed.name,
             'dateis': sl.created,
             'id': sl.id} for sl in slist]

        self.assertEqual(siting_list, expected_list)

    def test_get_siting_details_by_id(self):
        pid = 1
        slist = SitingList.objects.filter(id=pid)
        siting_list = get_siting_details(pid)
        expected_list = [{'animal': sl.breed.animals.all()[0].name,
             'breed': sl.breed.name,
             'dateis': sl.created,
             'id': sl.id} for sl in slist]

        self.assertEqual(siting_list, expected_list)

    def test_save_siting_details_by_id(self):
        pid = 2
        data = {'breed': 1, "created": datetime.datetime.today()}
        slist = SitingList.objects.filter(id=2)
        siting_list = save_siting_list(data)
        expected_list = [{'animal': sl.breed.animals.all()[0].name,
             'breed': sl.breed.name,
             'dateis': sl.created,
             'id': sl.id} for sl in slist]

        self.assertEqual(siting_list, expected_list)
