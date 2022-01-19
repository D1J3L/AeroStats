from fileinput import close
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from random import sample
from django.shortcuts import render, redirect

from .models import Plane
from .forms import PlaneForm

def home(request):
  watchlist = Plane.objects.all()
  return render(request, 'home.html', { 'watchlist': watchlist })

class PlaneCreate(CreateView):
  model = Plane
  fields = ['icao24']
  success_url = '/www.google.com'

class PlaneUpdate(UpdateView):
  model = Plane
  fields = ['icao24']

class PlaneDelete(DeleteView):
  model = Plane
  success_url = '/planes/'

def add_plane(request):
  # create a ModelForm instance using the data in the posted form
  print('hello')
  print(request.POST)

  form = PlaneForm(request.POST)
  # validate the data
  if form.is_valid():
    new_plane = form.save(commit=False)
    print(new_plane)
    new_plane.save()
  return redirect('home')