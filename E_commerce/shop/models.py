from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20, blank=False)
    phone = models.IntegerField()
    email_address = models.EmailField(blank=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=25)
    age = models.IntegerField(blank=False)
    phone = models.IntegerField()

    def __str__(self):
        return self.first_name


class School(models.Model):
    name = models.CharField(max_length=47)
    location = models.CharField(max_length=56)
    level = models.CharField(max_length=40, blank=False)

    def __str__(self):
        return self.name
