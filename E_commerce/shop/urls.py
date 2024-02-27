from . import views
from django.urls import path

urlpatterns = [
    path("", views.home),
    path("class/", views.clas),
    path("adm/", views.adm),
    path("name/", views.namee),
    path("DOB/", views.dob),
    path("student_list", views.students_list)

]
