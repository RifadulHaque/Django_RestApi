from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    courseID = models.CharField(max_length=10)
    grade = models.CharField(max_length=2)

