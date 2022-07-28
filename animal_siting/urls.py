# Django import
from django.urls import path

# Local Import
from . import views


urlpatterns = [
    path('home/', views.index, name='index'),
    path('get-breeds/', views.get_breeds, name='get_breed_dynamic'),
    path('get-breed-data/', views.get_breeds_html),
    path('add-siting-list/', views.add_siting_list, name='add_siting_list_dynamic'),
    path('remove-siting-list/', views.remove_siting_list, name='remove_siting_list_dynamic'),
    path('', views.siting_list_home, name="siting_list_home"),
    path('manage-siting-list/', views.manage_siting_list),
    path('manage-siting-list/<int:id>', views.manage_siting_list),
    path('get-form/', views.add_siting_list_form)
]