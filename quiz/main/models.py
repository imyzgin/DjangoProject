from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class Quiz(models.Model):
#    user = models.ManyToOneRel(User)

#class Question(models.Model):
#    quiz = models.ManyToManyField(Quiz)
#    points = models.IntegerField()
#    correct_answer = models.ForeignKey('AnswerVariant')


#class AnswerVariant(models.Model):
#    quizes = models.ManyToManyField(Question)
#    text = models.TextField()

class Author(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    dateOfBirth = models.DateField()
    dateOfDeath = models.DateField()
    

class Book(models.Model):
    bookName = models.CharField(max_length=200)
    yearOfPublication = models.IntegerField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE) #????
    genre = models.ManyToManyField('Genre') 


class Genre(models.Model):
    genreName = models.CharField(max_length=200)