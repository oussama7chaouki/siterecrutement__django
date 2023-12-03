from django.db import models
from shared.models import User

class Skill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=255)

class Language(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=255)

class Formation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    formation = models.CharField(max_length=255)
    school = models.CharField(max_length=255, null=True, blank=True)
    startyear = models.IntegerField(null=True, blank=True)
    endyear = models.IntegerField(null=True, blank=True)

class Experience(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    startyear = models.DateField()
    endyear = models.DateField(null=True, blank=True) 

class Information(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=250, null=True, blank=True)
    prenom = models.CharField(max_length=250, null=True, blank=True)
    ville = models.CharField(max_length=250)
    date = models.DateField()
    tel = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=191, null=True, blank=True)
    _select = models.CharField(max_length=100, null=True, blank=True)  # Using _select due to reserved word 'select'
    cv = models.FileField(upload_to='cv/', null=True)