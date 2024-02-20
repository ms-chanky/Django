from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name='home'),
    path('about/', views.about),
    path('contact/', views.contact)
]

