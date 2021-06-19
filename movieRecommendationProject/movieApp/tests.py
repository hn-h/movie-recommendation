from django.test import TestCase
from django.urls import reverse
from .models import Movie, MovieIDs
from movieApp import views

FORM_URL=reverse("home")

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

    def test_get_movies(self):
        movies = views.getMovies('Action',2000,8,30000)
        self.assertTrue(movies)

    def test_form_and_scrape(self):
        """Test that form gets the inputs normally and pass the scrape"""
        form_data={
            'year':2000,
            'rate':8,
            'genres':'Action',
            'votes':30000
        }

        request = self.client.post(FORM_URL,form_data)
        self.assertTrue(getattr(MovieIDs.objects.first(), 'movId'))
