from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserReviewForm

#un cristo
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'index')  
            return redirect(next_url)
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'users/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserRegistrationForm()
    return render(request, 'users/form.html', {'form': form})

@login_required(login_url="/users/login/")
def review_view(request):
    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserReviewForm()
    return render(request, 'users/review.html', {'form': form})

@login_required(login_url="/users/login/")
def logout_view(request):
    logout(request)
    return redirect('index')

#basura de sessions en blog site que no se ni si haré aqui, BORRAR
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Review

class SingleReviewView(DetailView):
    template_name = "users/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")  
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context

@login_required
def add_favorite(request):
    if request.method == "POST":
        review_id = request.POST.get("review_id")
        if review_id:
            request.session["favorite_review"] = review_id  
    return redirect("single_review", pk=review_id)


