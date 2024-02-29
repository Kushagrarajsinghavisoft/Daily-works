from django.contrib import admin

# Register your models here.
from .models import Student
admin.site.register(Student)   #registering Student model on admin panel