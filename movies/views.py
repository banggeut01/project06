from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Movie
from .forms import MovieForm, ReviewForm
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie = movie_form.save()
            return redirect('movies:detail', movie.pk)
    else:
        movie_form = MovieForm()
    context = {
        'movie_form': movie_form
    }
    return render(request, 'movies/form.html', context)

def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    review_form = ReviewForm()
    context = {
        'movie': movie,
        'review_form': review_form
    }
    return render(request, 'movies/detail.html', context)

def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie = movie_form.save()
            return redirect('movies:detail', movie.pk)
    else:
        movie_form = MovieForm(instance=movie)
    context = {
        'movie_form': movie_form
    }
    return render(request, 'movies/form.html', context)

@require_POST
def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movies:index')

@require_POST
def review_create(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.movie = movie
        review.save()
    return redirect('movies:detail', movie.pk)