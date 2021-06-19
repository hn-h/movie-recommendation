from django.test import TestCase
from .models import Movie

class TestMovie(TestCase):
    """General test cases for the project"""
    def test_movie_model(self):
        """Make sure that movie model migrated and working normally"""
        testMovie=Movie()
        testMovie.movieID='ID5321'
        testMovie.name='Movie Name'
        testMovie.year=2001
        testMovie.genres='Action'
        testMovie.image='https://cdn.britannica.com/78/194178-050-7ABF2B15/Emma-Stone-La-Land-Damien-Chazelle.jpg'
        testMovie.link='https://www.imdb.com/title/tt7638348/'
        testMovie.plot='A retired Special Forces officer is trapped in a never-ending time loop on the day of his death.'
        testMovie.rate=6.9
        testMovie.votes=31000
        testMovie.save()

        self.assertEqual(getattr(Movie.objects.first(), 'name'), 'Movie Name')
        self.assertEqual(getattr(Movie.objects.first(), 'movieID'), 'ID5321')