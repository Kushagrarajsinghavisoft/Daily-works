from django.shortcuts import render,redirect
from basic_app.forms import UserForm, UserProfileInfoForm, TodoForm

# importing necessary files from django libraries
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

#created index view for the main page
def index(request):
    return render(request,'basic_app/index.html')

#created user_logout view for user to logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))  #after logging out redirect to main page(index)

#created register view for user registration
def register(request):
    registered=False      #assigning registered to false at first

    if request.method=='POST':    #checking for method if it is post
        user_form=UserForm(data=request.POST)   #created an object of class UserForm
        profile_form=UserProfileInfoForm(data=request.POST)   #created an object of class UserProfileInfoForm

        if user_form.is_valid() and profile_form.is_valid():  #check if both objects are valid or not

            user=user_form.save()     #save the data stored in object

            user.set_password(user.password)    #it will go to the settigs.py file and Set and hash the user's password 
            user.save()

            profile = profile_form.save(commit=False)  #it will save the data but will not commit to the database
            profile.user=user      #building one to one relationship

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()   #now save the data

            registered=True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'basic_app/registration.html',{ 'user_form':user_form,
                                                         'profile_form':profile_form,
                                                          'registered':registered})


def user_login(request):
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('create_view'))
            else:
                return HttpResponse("User is not Active!")
        else:
            print("Someone tried to login and failed!")
            print("Username {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'basic_app/login.html', {})



from .models import Todo

def create_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_view')  # Redirect to the same view after saving the form
    else:
        form = TodoForm()

    allTodo = Todo.objects.all()  # Fetch all todos from the database

    return render(request, 'basic_app/create_view.html', {'form': form, 'allTodo': allTodo})



def update(request, sno):
    # Handling POST request to update a Todo
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        todo = Todo.objects.filter(sno=sno).first()
        todo.title = title
        todo.desc = desc
        todo.save()
        return redirect('create_view')

    # Fetching the Todo item to be updated
    todo = Todo.objects.filter(sno=sno).first()
    return render(request, 'basic_app/update.html', {'todo': todo})


def delete(request, sno):
    # Fetching the Todo item to be deleted
    todo = Todo.objects.get(sno=sno)
    
    # Deleting the Todo item from the database
    todo.delete()
    
    # Redirecting back to the main page
    return redirect("create_view")
