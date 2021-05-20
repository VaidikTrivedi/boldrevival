from django.contrib import admin

# Register your models here.
from .models import Volunteer, Organization, Investor

admin.site.register(Volunteer)
admin.site.register(Organization)
admin.site.register(Investor)