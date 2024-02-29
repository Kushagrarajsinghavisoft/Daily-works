
    # Create your models here.

from django.db import models

#creating a table named Student in database
class Student(models.Model):
    name = models.CharField(max_length=50)   #name field with char type and constrain of maximum 50 length
    age = models.IntegerField()     #age field with integer type and no constrain
    roll_no = models.IntegerField(primary_key=True)     #roll number field with integer type and primary key constrain
    courses = models.CharField(max_length=250)      #courses field with char type and constrain of maximum 250 length

    def __str__(self):
        #it returns the string representation of the 'name' attribute.
        return str(self.name)