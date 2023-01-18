from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('demand', views.demand),
    path('geography', views.geography),
    path('skills', views.skills),
    path('recent_vacancies', views.recent_vacancies),
]
