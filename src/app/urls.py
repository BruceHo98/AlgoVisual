from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='visualisation'),
    path('about/', views.about, name='about'),
    path('sorting/', views.sorting, name='sorting'),
    path('graph/', views.graph, name='graph'),
    path('dynamic_programming/', views.dynamic_programming, name='dynamic_programming'),
    path('machine_learning/', views.machine_learning, name='machine_learning'),
]