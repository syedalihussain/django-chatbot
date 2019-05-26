from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=200)


class Question(models.Model):
    text = models.CharField(max_length=200)


class Answer(models.Model):
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
