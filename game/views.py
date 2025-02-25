from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Update
#AYUDA
def index(request):
    return render(request, 'game/index.html')

# @login_required(login_url="/users/login/")
def about(request):
    return render(request, 'game/about.html')

# @login_required(login_url="/users/login/")
def trailer(request):
    return render(request, 'game/trailer.html')

# @login_required(login_url="/users/login/")
def updates(request):
    updates = Update.objects.all()
    return render(request, 'game/updates.html', {'updates': updates})

# @login_required(login_url="/users/login/")
def team(request):
    return render(request, 'game/team.html')

@login_required(login_url="/users/login/")
def leaderboard(request):
    return render(request, 'game/leaderboard.html')

@login_required(login_url="/users/login/")
def jump_game(request):
    return render(request, 'game/jump_game.html')

@login_required #esto ya veré si hacerlo o no
def single_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    favorite_id = request.session.get("favorite_review") 
    is_favorite = str(review.id) == str(favorite_id) 

    return render(request, "game/single_review.html", {"review": review, "is_favorite": is_favorite})

