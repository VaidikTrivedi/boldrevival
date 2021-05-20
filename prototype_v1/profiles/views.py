from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, unauthenticated_user

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'volunteer'])
def home(request):
    return render(request, 'profiles/home.html')


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login Credentials Wrong! Please try again')
            return redirect('login')

    return render(request, 'profiles/login.html')


@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Registration Success!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'profiles/register.html', context)