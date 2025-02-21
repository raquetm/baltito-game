from django.shortcuts import render
from .models import Update

def index(request):
    return render(request, 'game/index.html')

def about(request):
    return render(request, 'game/about.html')

def trailer(request):
    return render(request, 'game/trailer.html')

def updates(request):
    updates = Update.objects.all().order_by('-date')
    return render(request, 'game/updates.html', {'updates': updates})

def team(request):
    return render(request, 'game/team.html')

def play_game(request):
    return render(request, 'game/play_game.html')

def leaderboard(request):
    scores = UserScore.objects.all().order_by('-score')
    return render(request, 'game/leaderboard.html', {'scores': scores})