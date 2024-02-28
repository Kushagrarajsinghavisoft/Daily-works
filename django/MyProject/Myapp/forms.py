from django import forms
from Myapp.models import Student

class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields=[
            "name",
            "age",
            "roll_no",
            "courses"
        ]