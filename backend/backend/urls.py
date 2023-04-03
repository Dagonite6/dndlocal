from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'zalupa', AuthView, basename='uebok')

# urlpatterns = router.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('character/', include('character.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)