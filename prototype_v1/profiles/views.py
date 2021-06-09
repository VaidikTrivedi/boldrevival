from .models import Investor, Organization, Volunteer
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, CompleterProfile_Volunteer, CompleteProfile_Organization, CompleteProfile_Investor
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from .decorators import allowed_users, unauthenticated_user

# Create your views here.

# user_id = 0

# @allowed_users(allowed_roles=['admin', 'volunteer'])
def home(request):
    return render(request, 'profiles/home.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
        #print(user.is_authenticated)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login Credentials Wrong! Please try again')
            return redirect('login')

    return render(request, 'profiles/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, 'Registration Success!')
            user = authenticate(request, username=username, password=password)
            #print("\n\n", username, password, user, "IF STARTTING \n\n")
            if user is not None:
                login(request, user)
                print("\n\n\n\nIN IF", request.user.id, "\n\n\n")
                return redirect('profile_setup')
            else:
                return redirect('register')

    context = {'form': form}
    return render(request, 'profiles/register.html', context)


def profile_setup(request):
    form = CompleterProfile_Volunteer()
    form1 = CompleteProfile_Organization()
    form2 = CompleteProfile_Investor()

    if request.method == 'POST':
        form = CompleterProfile_Volunteer(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            education = form.cleaned_data.get('education')
            occupation = form.cleaned_data.get('occupation')
            #print(name, phone, email, education, occupation)
            n = Volunteer.objects.count()
            if n == None:
                n = 1
            else:
                n = n+1

            volunteer = Volunteer(request.user.id, n, name, phone, email, education, occupation)
            volunteer.save()
            user = User.objects.get(id = request.user.id)
            group = Group.objects.get(name='volunteer')
            #print(volunteer.id, group)
            group.user_set.add(user)
            messages.success(request, 'Profile Setup Completed, Please Login again!')
            return redirect('login')

        form1 = CompleteProfile_Organization(request.POST)
        if form1.is_valid():
            name = form1.cleaned_data.get('name')
            phone = form1.cleaned_data.get('phone')
            email = form1.cleaned_data.get('email')
            sector = form1.cleaned_data.get('sector')
            #print(name, phone, email, sector)
            n = Organization.objects.count()
            if n == None:
                n = 1
            else:
                n = n+1

            print("\n\n\n", request.user.id, "\n\n\n")
            organization = Organization(request.user.id, n, name, phone, email, sector)
            organization.save()
            user = User.objects.get(id = request.user.id)
            group = Group.objects.get(name='organization')
            #print(organization.id, group)
            group.user_set.add(user)
            messages.success(request, 'Profile Setup Completed, Please Login again!')
            return redirect('login')

        form2 = CompleteProfile_Investor(request.POST)
        if form2.is_valid():
            name = form2.cleaned_data.get('name')
            phone = form2.cleaned_data.get('phone')
            email = form2.cleaned_data.get('email')
            type = form2.cleaned_data.get('types')
            print(name, phone, email, type)
            n = Investor.objects.count()
            if n == None:
                n = 1
            else:
                n = n+1
            investor = Investor(request.user.id, n, name, phone, email, type)
            investor.save()
            user = User.objects.get(id = request.user.id)
            group = Group.objects.get(name='investor')
            group.user_set.add(user)
            messages.success(request, 'Profile Setup Completed, Please Login again!')
            return redirect('login')
        
    context = {'form': form, 'form1': form1, 'form2': form2}
    return render(request, 'profiles/profile_setup.html', context=context)