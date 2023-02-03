from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def hobbies_index(request):
  return render(request, 'hobbies/index.html', {'hobbies': hobbies})

class Hobby:
  def __init__(self, name, level, description, price):
    self.name = name
    self.level = level
    self.description = description
    self.price = price

hobbies = [
  Hobby('Woodworking', 'Beginner', 'building things with your hands', 6)
]