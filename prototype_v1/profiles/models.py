from django.db import models

# Create your models here.

class Volunteer(models.Model):
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
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=50, null=True)
    education = models.CharField(max_length=100, null=True, choices=EDUCATION)
    occupation = models.CharField(max_length=100, null=True, choices=OCCUPATION)
    date_created = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    SECTOR = (
             ('private sector', 'Private Sector'),
             ('public sector', 'Public Sector'),
             ('third sector', 'Third Sector'),
             )
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15,null=True)
    email = models.CharField(max_length=50, null=True)
    sector = models.CharField(max_length=100, null=True, choices=SECTOR)
    date_created = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Investor(models.Model):
    TYPES = (
            ('type1', 'Type1'),
            ('type2', 'Type2'),
            )
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15,null=True)
    email = models.CharField(max_length=50, null=True)
    types = models.CharField(max_length=100, null=True, choices=TYPES)
    date_created = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name