from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'title': 'AlgoVisual'})

def about(request):
    return render(request, 'about.html', {'title': 'About'})

def sorting(request):
    return render(request, 'sorting.html', {'title': 'Sorting'})

def graph(request):
    return render(request, 'graph.html', {'title': 'Graph'})

def dynamic_programming(request):
    return render(request, 'dynamic_programming.html', {'title': 'Dynamic Programming'})

def machine_learning(request):
    return render(request, 'machine_learning.html', {'title': 'Machine Learning'})

# Create your views here.
