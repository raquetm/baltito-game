from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import Update, UserScore
from users.models import UserProfile

# vista para la página de inicio
class IndexView(TemplateView):
    template_name = 'game/index.html'

# vista para la página About us
class AboutView(TemplateView):
    template_name = 'game/about.html'

# vista para la página del tráiler del juego
class TrailerView(TemplateView):
    template_name = 'game/trailer.html'

# vista para mostrar las actualizaciones 
class UpdatesView(ListView):
    model = Update
    template_name = 'game/updates.html'
    context_object_name = 'updates'

# vista para la página del equipo de desarrollo
class TeamView(TemplateView):
    template_name = 'game/team.html'

# vista para el ranking de jugadores 
@method_decorator(login_required(login_url="/users/login/"), name='dispatch')
class LeaderboardView(ListView):
    model = UserScore
    template_name = 'game/leaderboard.html'
    context_object_name = 'scores'

    def get_queryset(self):
        scores = UserScore.objects.all().order_by('-score')[:15]  
        print(f"Scores in DB: {scores}")  
        return scores

# vista del juego 
@method_decorator(login_required(login_url="/users/login/"), name='dispatch')
class JumpGameView(TemplateView):
    template_name = 'game/jump_game.html'

# función para guardar la puntuación de un usuario
@login_required
def save_score(request):
    if request.method == "POST":  
        score = request.POST.get('score')  
        if score:
            user = request.user  
            UserScore.objects.create(user=user.userprofile, score=score) # guarda la puntuación en la base de datos

            return redirect('leaderboard')  # redirige a la tabla de clasificación

    return redirect('home') 
