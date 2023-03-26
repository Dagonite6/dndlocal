from django.urls import path, include
from .views import RegisterView, LoginView
from knox import views as knox_views

urlpatterns = [
    # path('/', include('knox.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
]