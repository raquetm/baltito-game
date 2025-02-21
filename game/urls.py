from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('trailer/', views.trailer, name='trailer'),
    path('updates/', views.updates, name='updates'),
    path('team/', views.team, name='team'),
    path('play/', views.play_game, name='play_game'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]