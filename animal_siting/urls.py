# Django import
from django.urls import path

# Local Import
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('get-breeds/', views.get_breeds, name='get_breed_dynamic'),
    path('add-siting-list/', views.add_siting_list, name='add_siting_list_dynamic'),
    path('remove-siting-list/', views.remove_siting_list, name='remove_siting_list_dynamic')
]