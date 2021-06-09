from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import AbstractUser, User
#from profiles.models import Volunteer, Organization, Investor

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CompleterProfile_Volunteer(forms.Form):
    EDUCATION = (
                ('primary school degree', 'Primary School Degree'),
                ('high school degree', 'High School Degree'),
                ('college degree', 'College Degree'),
                ('master degree', 'Master Degree'),
                ('phd degree', 'PhD Degree'),
                )
    OCCUPATION = (
                ('unemployeed', 'Unemployeed'),
                ('student', 'Student'),
                ('recent graduate', 'Recent Graduate'),
                ('business owner', 'Business Owner'),
                ('private job', 'Private Job'),
                ('goverment job', 'Goverment Job'),                               
                )
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=200)
    phone = forms.CharField(max_length=14)
    education = forms.CharField(widget=forms.Select(choices=EDUCATION))
    occupation = forms.CharField(widget=forms.Select(choices=OCCUPATION))

class CompleteProfile_Organization(forms.Form):
    SECTOR = (
             ('private sector', 'Private Sector'),
             ('public sector', 'Public Sector'),
             ('third sector', 'Third Sector'),
             )
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    email = forms.CharField(max_length=50)
    sector = forms.CharField(widget=forms.Select(choices=SECTOR))

class CompleteProfile_Investor(forms.Form):
    TYPES = (
            ('type1', 'Type1'),
            ('type2', 'Type2'),
            )
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    email = forms.CharField(max_length=50)
    types = forms.CharField(widget=forms.Select(choices=TYPES))
