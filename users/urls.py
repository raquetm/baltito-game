from django.urls import path
from . import views
from .views import SingleReviewView, add_favorite


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('review/', views.review_view, name='review'),

    # Nueva ruta para favoritos
    path("review/<int:pk>/", SingleReviewView.as_view(), name="single_review"),
    path("favorite/", add_favorite, name="add_favorite"),
]
