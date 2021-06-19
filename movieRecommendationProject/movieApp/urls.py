from django.urls import path
from movieApp import views

urlpatterns = [
    path('',views.formView,name='home'),
    path('<int:pk>',views.MovieDetailView.as_view(),name='movie_detail'),
    path('next',views.nextMov,name='next'),
]
