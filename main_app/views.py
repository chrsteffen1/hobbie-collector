from django.shortcuts import render
from .models import Hobby

# Create your views here.
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def hobbies_index(request):
  hobbies = Hobby.objects.all()
  return render(request, 'hobbies/index.html', {'hobbies': hobbies})

