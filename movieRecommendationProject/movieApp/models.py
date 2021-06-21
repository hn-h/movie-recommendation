from django.db import models

class Movie(models.Model):
    """Movie model which contains the interested data fields of the movie"""
    movieID=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    year=models.IntegerField()
    genres=models.CharField(max_length=30)
    image=models.URLField(max_length=200)
    link=models.URLField(max_length=200)
    plot=models.TextField()
    rate=models.FloatField()
    votes=models.IntegerField()

    def __str__(self):
        return self.name

class MovieIDs(models.Model):
    """IDs model is used to save IDs of the filtered movies"""
    movId=models.CharField(max_length=30)
    def __str__(self):
        return self.movId

class MovieDB(models.Model):
    movieID=models.CharField(max_length=30)
    year=models.IntegerField()
    genres=models.CharField(max_length=30)
    rate=models.FloatField()
    votes=models.IntegerField()

    def __str__(self):
        return self.movieID
