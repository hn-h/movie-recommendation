from django import forms
from movieApp.models import Movie

#Choices for gernes
choices=[('Action','Action'),
         ('Comedy','Comedy'),
         ('Drama','Drama'),
         ('Sci-Fi','Sci-Fi'),
         ('Horror','Horror'),
         ('Animation','Animation'),
         ('Fantasy','Fantasy'),
         ('Documentary','Documentary')]

class FilterForm(forms.ModelForm):
    """User preferences input form"""
    genres=forms.ChoiceField(choices=choices, widget=forms.RadioSelect())
    class Meta:
        model=Movie
        fields=['year','rate','genres','votes']
