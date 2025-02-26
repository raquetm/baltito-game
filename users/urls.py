from django.urls import path
from .views import LoginView, LogoutView, RegisterView, ReviewView, SingleReviewView, AddFavoriteView, ReviewListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('review/', ReviewView.as_view(), name='review'),
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('review/<int:pk>/', SingleReviewView.as_view(), name='single_review'),
    path('add_favorite/', AddFavoriteView.as_view(), name='add_favorite'),
]