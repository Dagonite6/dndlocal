from django.urls import path, include
from users import views
from knox import views as knox_views

urlpatterns = [
    path('/', include('knox.urls')),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'), #invalidate all active tokens for the user
]