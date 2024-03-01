from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from .models import Student
from .forms import Studentform

def create_view(request):    
    context = {}      #to pass data from view to template

    # Create an instance of the Studentform
    form = Studentform(request.POST)

    # Check if the form is valid
    if form.is_valid():
        # Save the form data to the database
        form.save()

        # Redirect to the home page after successful form submission
        return HttpResponseRedirect("/")
    
    context['form'] = form
    return render(request, "create_view.html", context)    #to generate a HTTP response by rendering the specified HTML template (create_view.html)


def list_view(request):
    context = {}       #to pass data from view to template

    # Retrieve all student objects from the database
    context["dataset"] = Student.objects.all()
         
    return render(request, "list_view.html", context)

def detail_view(request, id):
    context = {}    #to pass data from view to template

    # Retrieve a specific student object based on the roll_no
    

    return render(request, "detail_view.html", context)     #to generate a HTTP response by rendering the specified HTML template (detail_view.html)

def update_view(request, id):
    context = {}    #to pass data from view to template
    
    # Retrieve the specific student object to be updated
    obj = get_object_or_404(Student, roll_no=id)

    # Create an instance of the Studentform with the retrieved object data
    form = Studentform(request.POST, instance=obj)

    # Check if the form is valid
    if form.is_valid():
        # Save the updated form data to the database
        form.save()

        # Redirect to the detail view of the updated student
        return HttpResponseRedirect("/" + id)
    
    context['form'] = form
    return render(request, "update_view.html", context)     #to generate a HTTP response by rendering the specified HTML template (update_view.html)

def delete_view(request, id):
    context = {}    #to pass data from view to template

    # Retrieve the specific student object to be deleted
    obj = get_object_or_404(Student, roll_no=id)

    # Check if the request method is POST (indicating a form submission)
    if request.method == "POST":
        # Delete the student object from the database
        obj.delete()

        # Redirect to the home page after successful deletion
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)     #to generate a HTTP response by rendering the specified HTML template (delete_view.html)
