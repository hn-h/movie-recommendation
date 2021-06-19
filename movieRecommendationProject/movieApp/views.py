from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from movieApp.models import Movie,MovieIDs
from movieApp.forms import FilterForm
import pandas as pd
import requests
from bs4 import BeautifulSoup as BSoup
import json
import random

def loadData():
    """Load the data file which we will movie ID from to start Scraping"""
    df=pd.read_csv('movieApp/new_imdb_dataset.csv', header=0, dtype='unicode')
    return df

def getMovies(genre,year,rate,votes):
    """Filter the data by user preferences and retern movies IDs"""
    df=loadData()
    suggested_df=df[(df.genres.str.contains(genre,na=False))&(df.startYear.astype(int)>=year)&(df.averageRating.astype(float)>=rate)&(df.numVotes.astype(int)>=votes)]
    return(list(suggested_df.tconst))

def scrape(request,suggested_movie_id):
    """Using Movie ID to Scrape IMDB website, get needed movie data and save in Movie model"""
    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    url = "https://www.imdb.com/title/"+suggested_movie_id
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    movie_details=json.loads(soup.find(type="application/ld+json").contents[0])
    #In case scraped json has any error used try-except
    try:
        suggested_movie=Movie()
        suggested_movie.movieID=suggested_movie
        suggested_movie.name=movie_details["name"]
        suggested_movie.year=movie_details["datePublished"].split('-')[0]
        suggested_movie.genres=movie_details["genre"]
        suggested_movie.image=movie_details["image"]
        suggested_movie.link='https://www.imdb.com' + movie_details["url"]
        suggested_movie.plot=movie_details["description"]
        suggested_movie.rate=movie_details["aggregateRating"]["ratingValue"]
        suggested_movie.votes=movie_details["aggregateRating"]["ratingCount"]
        suggested_movie.save()
        MovieIDs.objects.filter(movId=suggested_movie_id).delete()
    except KeyError:
        MovieIDs.objects.filter(movId=suggested_movie_id).delete()
        nextMov(request)

class MovieDetailView(DetailView):
    """Our main view of each suggested movie"""
    model=Movie

def formView(request):
    """Form handling to get user preferences"""
    form = FilterForm()
    if request.method=='POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            year=form.cleaned_data['year']
            genre=form.cleaned_data['genres']
            rate=form.cleaned_data['rate']
            votes=int(form.cleaned_data['votes'])
            suggested_movies=getMovies(genre,year,rate,votes)
            MovieIDs.objects.all().delete()
            Movie.objects.all().delete()
            sample_length = 100 if len(suggested_movies)>=100 else len(suggested_movies)
            for id in random.sample(suggested_movies,sample_length):
                moviesIDs=MovieIDs()
                moviesIDs.movId=id
                moviesIDs.save()
            scrape(request,str(MovieIDs.objects.first()))
            return redirect('movie_detail',pk=Movie.objects.first().pk)

    return render(request,'movieApp/index.html',context={'form':form})

def nextMov(request):
    """Getting the next suggested movie"""
    scrape(request,str(MovieIDs.objects.first()))
    return redirect('movie_detail', pk=Movie.objects.last().pk)
