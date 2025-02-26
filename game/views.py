from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import Update, UserScore
from users.models import UserProfile

class IndexView(TemplateView):
    template_name = 'game/index.html'

class AboutView(TemplateView):
    template_name = 'game/about.html'

class TrailerView(TemplateView):
    template_name = 'game/trailer.html'

class UpdatesView(ListView):
    model = Update
    template_name = 'game/updates.html'
    context_object_name = 'updates'

class TeamView(TemplateView):
    template_name = 'game/team.html'

@method_decorator(login_required(login_url="/users/login/"), name='dispatch')
class LeaderboardView(ListView):
    model = UserScore
    template_name = 'game/leaderboard.html'
    context_object_name = 'scores'

    def get_queryset(self):
        scores = UserScore.objects.all().order_by('-score')[:20] 
        print(f"Scores in DB: {scores}")  
        return scores


@method_decorator(login_required(login_url="/users/login/"), name='dispatch')
class JumpGameView(TemplateView):
    template_name = 'game/jump_game.html'

@login_required
def save_score(request):
    if request.method == "POST":
        score = request.POST.get('score')
        if score:
            user = request.user  # O usar el perfil del usuario si es necesario
            UserScore.objects.create(user=user.userprofile, score=score)

            # Redirige a la página de leaderboard después de guardar el puntaje
            return redirect('leaderboard')  # Reemplaza 'leaderboard' con la URL correcta si es necesario

    return redirect('home')

