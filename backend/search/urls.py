from django.urls import path
from . import views

urlpatterns = [
    path('races/', views.RaceListView.as_view(), name='RacesList'), #races list
    path('races/<int:pk>/', views.RaceDetailView.as_view(), name='RaceDetails'), #races details
]