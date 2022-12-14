# Python Import
import json


# Django Import
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.urls import reverse
from django.views.decorators.http import require_GET,require_http_methods

# Local Import
from .models import Animal, SitingList, Breed
from .forms import SitingListForm, SitingListForm2


@require_GET
def siting_list_home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html", {'siting_list': get_siting_details()})


@require_GET
def add_siting_list_form(request):
    return render(request, 'add-siting-list.html', {'form': SitingListForm()})


# Get Sitting list from Database
def get_siting_details(pid=None):
    if pid:
        siting_list = SitingList.objects.filter(id=pid).order_by('created')
    else:
        siting_list = SitingList.objects.all().order_by('created')

    return [{'animal': sl.breed.animals.all()[0].name,
             'breed': sl.breed.name,
             'dateis': sl.created,
             'id': sl.id}
            for sl in siting_list]


# Landing Page
def index(request):
    """ Index page for animals sitting """

    context = {
        'siting_list': get_siting_details(),
        'form_urls': {'get_breed_url': reverse('get_breed_dynamic'),
                      'save_list_url': reverse('add_siting_list_dynamic'),
                      'remove_list_url': reverse('remove_siting_list_dynamic')},
        'form': SitingListForm2()
    }

    return render(request, 'index.html', context)


# Get breed list AJAX
def get_breeds(request):

    if request.method == 'GET':
        animal_id = request.GET.get('animal')
        animal = Animal.objects.filter(id=animal_id)
        breeds = {breed.id: breed.name for breed in animal[0].breeds.all()}
        return JsonResponse(breeds)

    return None


# Get breed list AJAX
def get_breeds_html(request):
    breeds = {}
    if request.method == 'POST':
        animal_id = request.POST.get('animal')
        animal = Animal.objects.filter(id=animal_id)
        breeds = {breed.id: breed.name for breed in animal[0].breeds.all()}

    return render(request, "breed-list.html", {'breeds' : breeds})


# Add new siting list
def save_siting_list(data):

    # Check length of data for having enough pack
    if 'breed' in data and 'created' in data:
        breed_id = data.get('breed', None)
        created = data.get('created', None)

        breed_obj = Breed.objects.get(id=breed_id)
        slist_obj = SitingList(breed=breed_obj, created=created)
        slist_obj.save()

    return get_siting_details()


@require_http_methods(("POST","GET"))
def manage_siting_list(request, id=None):
    if request.method == 'POST':
        response_data = {
            'breed': request.POST.get('breed', None),
            'created': request.POST.get('created', None)
        }
        save_siting_list(response_data)

    if request.method == 'GET' and id is not None:
        slist = SitingList.objects.filter(id=id)
        slist.delete()

    resp = get_siting_details()

    return render(request, "siting-list-table.html", {'siting_list': resp})

# Add new siting list
def save_siting_list(data):

    # Check length of data for having enough pack

    if 'breed' in data and 'created' in data:
        breed_id = data.get('breed', None)
        created = data.get('created', None)

        breed_obj = Breed.objects.get(id=breed_id)
        slist_obj = SitingList(breed=breed_obj, created=created)
        slist_obj.save()
        return get_siting_details(slist_obj.pk)

    return False


# Add siting list data - AJAX
def add_siting_list(request):
    resp = False
    received_json_data = json.loads(request.body)
    if request.method == 'POST':
        resp = save_siting_list(received_json_data)

    response = {
        'data': resp,
        'msg': 'Failed to Save' if not resp else 'Saved Successfully'
    }

    return JsonResponse(response)


# Delete the siting list record - AJAX
def remove_siting_list(request):

    resp = False
    if request.method == 'GET':
        slist_id = request.GET.get('slist_id')
        slist = SitingList.objects.filter(id=slist_id)
        if slist.delete():
            resp = True

    resp = {
        'data': resp,
        'msg': 'Failed to Delete' if not resp else 'Deleted Successfully'
    }

    return JsonResponse(resp)
