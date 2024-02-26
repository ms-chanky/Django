from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("blog/", views.blog),
    path("blog-single/", views.single),
    path("portfolio/", views.portfolio)

    ]