from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('top-movies/', views.top_movies, name='top-movies'),
    path('newest/', views.estrenos, name='newest'),
    path('popular/', views.populares, name='popular'),
    path('movie/<int:movie_id>/', views.movie, name='movie'),
    path('search/', views.search, name='search'),
    path('genre/<category_name>/', views.category, name='category'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('account/', views.account, name='account'),

]
