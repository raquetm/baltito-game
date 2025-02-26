from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import FormView, DetailView, ListView
from .forms import UserRegistrationForm, UserReviewForm
from .models import Review

class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'index')
            return redirect(next_url)
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})

class RegisterView(FormView):
    template_name = 'users/form.html'
    form_class = UserRegistrationForm
    success_url = '/users/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(login_required(login_url="/users/login/"), name='dispatch')
class ReviewView(FormView):
    template_name = 'users/review.html'
    form_class = UserReviewForm
    success_url = '/reviews/' 

    def form_valid(self, form):
        review = form.save(commit=False)
        review.user = self.request.user  
        review.save()
        return super().form_valid(form)


@method_decorator(login_required(login_url="/users/login/"), name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

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

@method_decorator(login_required, name='dispatch')
class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST.get("review_id")
        if review_id:
            request.session["favorite_review"] = review_id
        return redirect("single_review", pk=review_id)

class ReviewListView(ListView):
    model = Review
    template_name = 'users/review_list.html'
    context_object_name = 'reviews'
