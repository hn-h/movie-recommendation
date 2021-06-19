from django import forms
from movieApp.models import Movie

#Choices for gernes
choices_genres=[('Action','Action'),
         ('Comedy','Comedy'),
         ('Drama','Drama'),
         ('Sci-Fi','Sci-Fi'),
         ('Horror','Horror'),
         ('Animation','Animation'),
         ('Fantasy','Fantasy'),
         ('Documentary','Documentary')]

choices_votes = [(20000,'More than 20,000'),
                 (50000,'More than 50,000'),
                 (100000,'More than 100,000'),
                 (200000,'More than 200,000')]

class FilterForm(forms.ModelForm):
    """User preferences input form"""
    genres=forms.ChoiceField(choices=choices_genres, widget=forms.RadioSelect())
    votes=forms.ChoiceField(choices=choices_votes, widget=forms.Select())
    class Meta:
        model=Movie
        fields=['year','rate','genres','votes']
