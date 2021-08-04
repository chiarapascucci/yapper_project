from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rango.models import Category, Page, Sport, Competition, Participation, Award, Breed, Dog
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from datetime import datetime

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    context_dict['extra'] = 'From the model solution on GitHub'
    
    visitor_cookie_handler(request)

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # Spoiler: now you DO need a context dictionary!
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
    
    return render(request, 'rango/category.html', context=context_dict)

@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:index'))
        else:
            print(form.errors)
    
    return render(request, 'rango/add_category.html', {'form': form})

@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None
    
    # You cannot add a page to a Category that does not exist... DM
    if category is None:
        return redirect(reverse('rango:index'))

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)  # This could be better done; for the purposes of TwD, this is fine. DM.
    
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)


@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:index'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    
    request.session['visits'] = visits



"""
 ====================== 
 Yapper views 
 ====================== 
"""
def breed_homepage(request):

    bhome_context = {}

    try:
        breeds = Breed.objects.all()

        bhome_context['breeds'] = breeds

    except Breed.DoesNotExist:
        bhome_context['breeds'] = None

    return render(request, 'rango/yapper/breeds_homepage.html', bhome_context)

    
# Individual breed page
def breed_profile(request, breed_name_slug): 

    bprofile_context = {}

    try:
        breed = Breed.objects.get(slug=breed_name_slug)
        dogs = Dog.objects.filter(breed=breed)

        bprofile_context['dogs'] = dogs
        bprofile_context['breed'] = breed

    except Breed.DoesNotExist:
        bprofile_context['dogs'] = None
        bprofile_context['breed'] = None

    return render(request, 'rango/yapper/breed_profile.html', bprofile_context)


# Individual dog profile
def dog_profile(request, breed_name_slug, dog_name_slug):

    dprofile_context = {}

    try:
        breed = Breed.objects.get(slug=breed_name_slug)
        dogs = Dog.objects.filter(breed=breed)

        dprofile_context['dogs'] = dogs
        dprofile_context['breed'] = breed

    except Breed.DoesNotExist:
        dprofile_context['dogs'] = None
        dprofile_context['breed'] = None

    return render(request, 'rango/yapper/dog_profile.html', dprofile_context)

    
def add_dog(request):
    return render(request, 'rango/yapper/add_dog.html', {})


def sports_homepage(request):
    
    # Context dictionary to input any external variables into the HTML template
    context_dict = {}
   
    sports_list = Sport.objects.order_by('-name')
    context_dict['sports'] = sports_list

    return render(request, 'rango/yapper/sports_homepage.html', context_dict)

def sports_profile(request, sports_name_slug):

    # Context dictionary to input any external variables into the HTML template
    context_dict = {}

    # Get the sport instance associated with the sport_name_slug
    try:
        sport = Sport.objects.get(slug=sports_name_slug)
        context_dict['sport'] = sport

        # Get competitions of that sport
        competition_list = Competition.objects.filter(sport=sport)
        context_dict['competitions'] = competition_list

    except Sport.DoesNotExist:
        context_dict['sport'] = None
        context_dict['competitions'] = None

    return render(request, 'rango/yapper/sports_profile.html', context_dict)

def competition_homepage(request):

    # Context dictionary to input any external variables into the HTML template
    context_dict = {}
   
    competition_list = Competition.objects.order_by('-name')
    context_dict['competitions'] = competition_list

    return render(request, 'rango/yapper/competition_homepage.html', context_dict)


def competition_profile(request, competition_name_slug):
    
    # Context dictionary to input any external variables into the HTML template
    context_dict = {}

    # Get the sport instance associated with the sport_name_slug
    try:
        competition = Competition.objects.get(slug=competition_name_slug)
        context_dict['competition'] = competition
    except Competition.DoesNotExist:
        context_dict['competition'] = None

    return render(request, 'rango/yapper/competition_profile.html', context_dict)

def add_competition(request):
    return render(request, 'rango/yapper/add_competition.html', {})

def user_profile(request):
    return render(request, 'rango/yapper/user_profile.html', {})

def user_profile_edit(request):
    return render(request, 'rango/yapper/user_profile_edit.html', {})

def faq(request):
    return render(request, 'rango/yapper/faq.html', {})



