# Importing the necessary module for form creation in Django.
from django import forms

# Importing the Student model from the Myapp application.
from Myapp.models import Student

# Creating a form class named Studentform that inherits from forms.ModelForm.
class Studentform(forms.ModelForm):
    # The Meta class is used to provide additional information about the form.
    class Meta:
        # The 'model' attribute specifies which model the form is associated with.
        model = Student
        
        # The 'fields' attribute specifies which fields from the model should be included in the form.
        fields = [
            "name",      # Include the 'name' field in the form.
            "age",       # Include the 'age' field in the form.
            "roll_no",   # Include the 'roll_no' field in the form.
            "courses"    # Include the 'courses' field in the form.
        ]
