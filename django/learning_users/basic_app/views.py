from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# importing necessary files from django libraries
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

#created index view for the main page
def index(request):
    return render(request,'basic_app/index.html')

# def special(request):
#     return HttpResponse("You are logged in, Nice!")

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
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("User is not Active!")
        else:
            print("Someone tried to login and failed!")
            print("Username {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'basic_app/login.html', {})
