from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name='List'), #список персожаней
    path('create/', views.CreateView.as_view(), name='Create'), #post реквест для создания
    path('<int:pk>/', views.DetailView.as_view(), name='Details'), #на один эндпоинт у нас get, patch, put и delete реквесты
]