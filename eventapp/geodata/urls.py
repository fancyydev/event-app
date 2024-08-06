from .views import LocationsListView 
from django.urls import path

urlpatterns = [
    path('locationList', LocationsListView.as_view()),
]