from . import views
from django.urls import path

urlpatterns = [
    path("", views.Name),
    path('adm', views.adm),
    path('dob', views.dob),
    path('clas', views.clas)
]
