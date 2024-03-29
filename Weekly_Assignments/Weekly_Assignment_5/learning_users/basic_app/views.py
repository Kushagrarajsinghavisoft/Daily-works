from django.shortcuts import render,redirect
from basic_app.forms import UserForm, UserProfileInfoForm, TodoForm

# importing necessary files from django libraries
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Todo,UserProfileInfo

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

            user.set_password(user.password)    #it will go to the settigs.py file and hash the user's password 
            user.save()

            profile = profile_form.save(commit=False)  #it will save the data but will not commit to the database
            profile.user=user      #building one to one relationship

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()   #now save the data

            registered=True
            login(request,user)
            return redirect(reverse('create_view'))  #redirect it to the create_view
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    #rendering the registration page and passing the context like user_form, profile_form, registered
    return render(request,'basic_app/registration.html',{ 'user_form':user_form,
                                                         'profile_form':profile_form,
                                                          'registered':registered})


def user_login(request):
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')

        #authenticating user through inbuild function
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:    #checking if the user is still active
                login(request, user)   #its a built in function which will automatically login 'user'
                return HttpResponseRedirect(reverse('create_view'))   #after logging in redirecting to view page
            else:
                #if user is not active then this part will get executed
                return HttpResponse("User is not Active!")
        else:
            #if by mistake the password entered is incorrect then this part will be printed
            print("Someone tried to login and failed!")
            print("Username {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'basic_app/login.html', {})

@login_required
def create_view(request):
    user_profile = None  # Initialize user_profile with None
    
    if request.user.is_superuser:
        # If the user is a superuser, directly use the user's attributes
        is_superuser = True
        course = None  # Superusers don't have a course
    else:
        # If the user is not a superuser, retrieve the UserProfileInfo instance
        try:
            user_profile = UserProfileInfo.objects.get(user=request.user)
            is_superuser = False
            course = user_profile.course
        except UserProfileInfo.DoesNotExist:
            # Handle the case when UserProfileInfo does not exist for the user
            # Redirect or display an error message
            # For now, just set is_superuser to False and course to None
            is_superuser = False
            course = None

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            if not is_superuser:
                todo.course = course  # Assign the current user's course to the todo item
            todo.save()
            return redirect('create_view')
    else:
        form = TodoForm()

    # Filter todo items based on the current user's course, unless the user is a superuser
    if is_superuser:
        allTodo = Todo.objects.all()
    else:
        allTodo = Todo.objects.filter(course=course)
    return render(request, 'basic_app/create_view.html', {'form': form, 'allTodo': allTodo, 'user_profile': user_profile})



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
