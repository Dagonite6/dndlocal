from django.urls import path, include
from .views import ListView, CreateView

urlpatterns = [
    path('', ListView.as_view(), name='List'),
    path('create/', CreateView.as_view(), name='Create'),
]