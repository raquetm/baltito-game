from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserRegistrationForm, UserReviewForm
from .models import Review

# vista para el inicio de sesión
class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')  

    def post(self, request):
        username = request.POST['username']  
        password = request.POST['password']  
        user = authenticate(request, username=username, password=password)  # intenta autenticar 

        if user is not None:
            login(request, user)  # inicia la sesión
            next_url = request.GET.get('next', 'index')  # si hay una URL de "next" en la petición, redirige allí
            return redirect(next_url)
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})  
            # muestra el formulario con un error

# vista para el registro 
class RegisterView(FormView):
    template_name = 'users/form.html'  # muestra el form
    form_class = UserRegistrationForm  
    success_url = '/users/login/'  # redirige al inicio de sesión 

    def form_valid(self, form):
        form.save()  # guarda el usuario y su perfil
        return super().form_valid(form)  

# vista para enviar reseñas (autenticación)
@method_decorator(login_required(login_url="/users/login/"), name='dispatch')
class ReviewView(FormView):
    template_name = 'users/review.html'  
    form_class = UserReviewForm  
    success_url = '/users/reviews/'  

    def form_valid(self, form):
        review = form.save(commit=False)  # no guarda el formulario todavía
        review.user = self.request.user  # asigna el usuario actual como autor de la reseña
        review.save()  
        return super().form_valid(form)  

# vista para eliminar una reseña (autenticación)
@method_decorator(login_required(login_url="/users/login/"), name='dispatch')
class DeleteReviewView(DeleteView):
    model = Review
    success_url = reverse_lazy('review_list')  

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)  # solo permite eliminar las reseñas creadas por el usuario actual

# vista para actualizar una reseña (autenticación)
@method_decorator(login_required(login_url="/users/login/"), name='dispatch')
class UpdateReviewView(UpdateView):
    model = Review
    form_class = UserReviewForm
    template_name = 'users/review.html'
    success_url = reverse_lazy('review_list')  

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)  # solo permite actualizar las reseñas creadas por el usuario actual

# vista para cerrar sesión del usuario
@method_decorator(login_required(login_url="/users/login/"), name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)  # cierra la sesión del usuario
        return redirect('index')  

# vista para mostrar una única reseña
class SingleReviewView(DetailView):
    template_name = "users/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        loaded_review = self.object  # obtiene la reseña actual
        request = self.request
        favorite_id = request.session.get("favorite_review")  # obtiene el ID de la reseña favorita almacenada en la sesión
        context["is_favorite"] = favorite_id == str(loaded_review.id)  # comprueba si la reseña actual es la favorita del usuario
        return context

# vista para modificar el favorito de una reseña
@method_decorator(login_required, name='dispatch')
class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST.get("review_id")  # obtiene el ID de la reseña enviada por POST
        if review_id:
            if request.session.get("favorite_review") == review_id:  
                del request.session["favorite_review"]  # elimina la reseña de favoritos
            else:
                request.session["favorite_review"] = review_id  # marca la reseña como favorita
        return redirect("single_review", pk=review_id)  # redirige a la página de la reseña

# vista para mostrar la lista de reseñas
class ReviewListView(ListView):
    model = Review
    template_name = 'users/review_list.html'  
    context_object_name = 'reviews' 
