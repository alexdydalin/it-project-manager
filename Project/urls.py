from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('demand', include('main.urls')),
    path('geography', include('main.urls')),
    path('skills', include('main.urls')),
    path('recent_vacancies', include('main.urls')),
]
