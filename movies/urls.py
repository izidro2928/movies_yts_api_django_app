from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name="movies/password_reset.html"),
         name="password_reset"),
    path('accounts/password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name="movies/password_reset_done.html"),
         name="password_reset_done"),
    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="movies/password_reset_form.html"),
         name="password_reset_confirm"),
    path('accounts/password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="movies/password_reset_complete.html"),
         name="password_reset_complete"),

]
