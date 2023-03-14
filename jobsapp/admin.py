from django.contrib import admin
from .models import Job, Applicant
from accounts.models import User


# Register your models here.
admin.site.register(User)
admin.site.register(Job)
admin.site.register(Applicant)


