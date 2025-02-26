from django.urls import path
from .views import IndexView, AboutView, TrailerView, UpdatesView, TeamView, LeaderboardView, JumpGameView, save_score

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('trailer/', TrailerView.as_view(), name='trailer'),
    path('updates/', UpdatesView.as_view(), name='updates'),
    path('team/', TeamView.as_view(), name='team'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('jump_game/', JumpGameView.as_view(), name='jump_game'),
    path('save_score/', save_score, name='save_score'),
]