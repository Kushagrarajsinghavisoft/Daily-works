from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from .models import Student
from .forms import Studentform

def create_view(request):
    context={}

    form=Studentform(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    
    context['form']=form
    return render(request, "create_view.html", context)


def list_view(request):
    context={}
    context["dataset"] = Student.objects.all()
         
    return render(request, "list_view.html", context)

def detail_view(request,id):
    context={}
    context['data']=Student.objects.get(roll_no=id)
    return render (request, "detail_view.html",context)


def update_view(request,id):
    context={}
    obj=get_object_or_404(Student,roll_no=id)

    form=Studentform(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    context['form']=form
    return render(request,"update_view.html",context)

def delete_view(request,id):
    context={}
    obj=get_object_or_404(Student,roll_no=id)

    if request.method=="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request,"delete_view.html",context)
