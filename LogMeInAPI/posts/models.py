from django.db import models

# Create your models here.


class Post (models.Model):
    sEndpoint = models.CharField(max_length=40,default="https://secure.logmeinrescue.com/api/")
    sEmail = models.EmailField(max_length=254,default="gorkem.korkmaz@rigosis.com")
    sPwd = models.CharField(max_length=25,default="FhG8AWyWdgry8uTUVj65.")
    iSession = models.CharField(max_length=25,default=12345678)
    iNodeID = models.CharField(max_length=25,default=337366)
    sAuthCode = models.CharField(max_length=25,default="4ahx...80u0")


    def __str__(self):
        return Post.sEmail