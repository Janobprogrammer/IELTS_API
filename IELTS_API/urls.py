from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("part1/", include("part1.urls")),
    path("part2/", include("part2.urls")),
    path("part3/", include("part3.urls")),

    path('api/api-token-auth/', views.obtain_auth_token, name="api-token-auth"),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
