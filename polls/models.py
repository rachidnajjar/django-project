import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    texte = models.CharField(max_length=200)
    datePublication = models.DateTimeField('date publication')
    
    def estPublicationRecente(self):
        return self.datePublication >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.texte
    
    
    
class Choix(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    texte = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.texte
