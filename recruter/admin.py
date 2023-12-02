from django.contrib import admin
from .models import Job,Candidature
from shared.models import User
# Register your models here.
admin.site.register(User)
admin.site.register(Candidature)
admin.site.register(Job)
