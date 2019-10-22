from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=40)
    title_en = models.CharField(max_length=40)
    audience = models.IntegerField() 
    open_date = models.DateTimeField()
    genre = models.CharField(max_length=40)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    score = models.IntegerField()
