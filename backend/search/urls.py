from django.urls import path
from . import views

urlpatterns = [
    path('races/<int:pk>/', views.RaceDetailView.as_view(), name='RaceDetails'), #races details
    path('bgs/<int:pk>/', views.BackgroundDetailView.as_view(), name='BackgroundDetails'), #bg details
]