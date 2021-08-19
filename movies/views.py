from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt
import requests
from .form import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    data = []
    movies = []
    next_page = None
    pre_page = None
    try:
        page_num = request.GET.get('page', 1)
        page_num = int(page_num)
        next_page = None
        pre_page = None
        url = f'https://yts.mx/api/v2/list_movies.json?page={page_num}&limit=18'
        res = requests.get(url)
        json = res.json()
        data = json['data']
        movies = data['movies']

        movie_count = data['movie_count']
        limit = data['limit']

        total_pages = (movie_count + limit - 1) / limit
        total_pages = round(total_pages)

        if page_num < total_pages:
            next_page = page_num + 1

        if page_num >= 2:
            pre_page = page_num - 1
    except Exception:
        pass

    return render(request, 'movies/index.html', {
        "title": "Home",
        "description": "Toros movies the bes website to watch movies online for free",
        "movies": movies,
        "data": data,
        "next_page": next_page,
        "pre_page": pre_page,
    })


def top_movies(request):
    try:
        page_num = request.GET.get('page', 1)
        page_num = int(page_num)
        next_page = None
        pre_page = None

        url = f'https://yts.mx/api/v2/list_movies.json?minimum_rating=8&page={page_num}'
        res = requests.get(url)
        json = res.json()
        data = json['data']
        movies = data['movies']

        movie_count = data['movie_count']
        limit = data['limit']

        total_pages = (movie_count + limit - 1) / limit
        total_pages = round(total_pages)

        if page_num < total_pages:
            next_page = page_num + 1

        if page_num >= 2:
            pre_page = page_num - 1
    except Exception:
        return redirect(home)

    return render(request, 'movies/movies.html', {
        "title": "Top movies",
        "description": "Toros movies the bes website to watch movies online for free",
        "movies": movies,
        "data": data,
        "next_page": next_page,
        "pre_page": pre_page,
    })


def estrenos(request):
    try:
        page_num = request.GET.get('page', 1)
        page_num = int(page_num)
        next_page = None
        pre_page = None

        url = f'https://yts.mx/api/v2/list_movies.json?sort_by=year&page={page_num}&limit=18'
        print(url)
        res = requests.get(url)
        json = res.json()
        data = json['data']
        movies = data['movies']

        movie_count = data['movie_count']
        limit = data['limit']

        total_pages = (movie_count + limit - 1) / limit
        total_pages = round(total_pages)

        if page_num < total_pages:
            next_page = page_num + 1

        if page_num >= 2:
            pre_page = page_num - 1
    except Exception:
        return redirect(home)

    return render(request, 'movies/estrenos.html', {
        "title": "Newest movies",
        "description": "Toros movies the bes website to watch movies online for free",
        "movies": movies,
        "data": data,
        "next_page": next_page,
        "pre_page": pre_page,
    })


def populares(request):
    try:
        page_num = request.GET.get('page', 1)
        page_num = int(page_num)
        next_page = None
        pre_page = None

        url = f'https://yts.mx/api/v2/list_movies.json?sort_by=like_count&page={page_num}'
        res = requests.get(url)
        json = res.json()
        data = json['data']
        movies = data['movies']

        movie_count = data['movie_count']
        limit = data['limit']

        total_pages = (movie_count + limit - 1) / limit
        total_pages = round(total_pages)

        if page_num < total_pages:
            next_page = page_num + 1

        if page_num >= 2:
            pre_page = page_num - 1
    except Exception:
        return redirect(home)

    return render(request, 'movies/populares.html', {
        "title": "Popular movies",
        "description": "Toros movies the bes website to watch movies online for free",
        "movies": movies,
        "data": data,
        "next_page": next_page,
        "pre_page": pre_page,
    })


@xframe_options_exempt
def movie(request, movie_id):
    url = f'https://yts.mx/api/v2/movie_details.json?movie_id={movie_id}&with_cast=true'
    res = requests.get(url)
    json = res.json()
    data = json['data']['movie']

    # MOVIE SUGESTION
    su_url = f'https://yts.mx/api/v2/movie_suggestions.json?movie_id={movie_id}'
    su_res = requests.get(su_url)
    su_json = su_res.json()
    su_movies = su_json['data']['movies']

    genres = data['genres']
    m_genres = ''
    for genre in genres:
        m_genres += str(genre + ", ")
    m_genres = m_genres[:-2]

    return render(request, 'movies/movie.html', {
        "title": "Movie details",
        "description": "Toros movies the best website to watch movies online for free",
        "movie": data,
        "movies": su_movies,
        "genres": m_genres,
    })


def search(request):
    data = []
    movies = []
    next_page = None
    pre_page = None
    s = None
    message = None
    try:
        page_num = request.GET.get('page', 1)
        page_num = int(page_num)
        next_page = None
        pre_page = None
        s = request.GET.get('s')

        url = f'https://yts.mx/api/v2/list_movies.json?query_term={s}&page={page_num}'
        res = requests.get(url)
        json = res.json()
        data = json['data']
        movies = data['movies']

        movie_count = data['movie_count']
        limit = data['limit']

        total_pages = (movie_count + limit - 1) / limit
        total_pages = round(total_pages)

        if page_num < total_pages:
            next_page = page_num + 1

        if page_num >= 2:
            pre_page = page_num - 1
    except Exception:
        message = 'no results'

    return render(request, 'movies/search.html', {
        "title": "Search movie",
        "description": "Toros movies the bes website to watch movies online for free",
        "movies": movies,
        "next_page": next_page,
        "pre_page": pre_page,
        "s": s,
        "message": message,
        "data": data,
    })


def category(request, category_name):
    try:
        page_num = request.GET.get('page', 1)
        page_num = int(page_num)

        next_page = None
        pre_page = None

        url = f'https://yts.mx/api/v2/list_movies.json?genre={category_name}&sort_by=rating&page={page_num}&limit=18'
        res = requests.get(url)
        json = res.json()
        data = json['data']
        movies = data['movies']
        movie_count = data['movie_count']
        limit = data['limit']

        total_pages = (movie_count + limit - 1) / limit
        total_pages = round(total_pages)

        if page_num < total_pages:
            next_page = page_num + 1

        if page_num >= 2:
            pre_page = page_num - 1

    except ValueError:
        return redirect(home)

    return render(request, 'movies/categories.html', {
        "title": f'{category_name.capitalize()} movies',
        "description": "Toros movies the bes website to watch movies online for free",
        "movies": movies,
        "data": data,
        "category_name": category_name,
        "next_page": next_page,
        "pre_page": pre_page,
    })


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfuly you can now login!')
            return redirect('login')

    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'movies/register.html', context)


def login_page(request):
    login_error_message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            login_error_message = "Username or password is incorrect"

    return render(request, 'movies/login.html', {
        "login_error_message": login_error_message,
    })


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def account(request):
    return render(request, 'movies/account.html')
