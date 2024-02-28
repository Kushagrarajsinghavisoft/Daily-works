
    # Create your models here.

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    roll_no = models.IntegerField(primary_key=True)
    courses = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)