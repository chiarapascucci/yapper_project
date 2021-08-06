
from django.template.defaultfilters import slugify
from rango.models import UserProfile,User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rango.models import Category, Page, Sport, Competition, Participation, Award, Breed, Dog, GMap
from rango.forms import AddDogForm, CompetitionForm, UserForm, UserProfileForm, EditUserProfileForm
from datetime import datetime


def index(request):
    context_dict = {}

    breed_list = Breed.objects.order_by('-follows')[:10]
    sport_list = Sport.objects.order_by('-follows')[:10]

    for breed in breed_list:
        print(breed)
    
    for sport in sport_list:
        print(sport)

    context_dict['topbreeds'] = breed_list
    context_dict['sports'] = sport_list
    visitor_cookie_handler(request)

    try:
        username = request.user.get_username()
        print('printing username: ',username)
        user=User.objects.get(username=username)

        try:
            
            user_profile = UserProfile.objects.get_or_create(user=user)[0]
            print(user_profile.user_slug)
            context_dict['user_profile']= user_profile
        except UserProfile.DoesNotExist:
            print('no user here')
            return render(request, 'rango/index.html', context=context_dict)

    except User.DoesNotExist:
        print('user does not exist')
        return render(request, 'rango/index.html', context=context_dict)

    

    print(context_dict['user_profile'])
    print(user.is_authenticated)
    
    
    
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # Spoiler: now you DO need a context dictionary!
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/about.html', context=context_dict)


@login_required
def edit_profile(request, user_name_slug):
    form = EditUserProfileForm()

    if request.method == 'POST':
        form = EditUserProfileForm(request.POST,request.FILES, instance=UserProfile.objects.get(user_slug=user_name_slug))
        if form.is_valid():
           form.save(commit=True)
           return redirect(reverse('rango:user', kwargs= {'user_name_slug': user_name_slug}))
        else:
            print(form.errors)
        return redirect(reverse('rango:user', kwargs= {'user_name_slug': user_name_slug})) 
    else:
        form = EditUserProfileForm(instance=UserProfile.objects.get(user_slug=user_name_slug))
        context_dict = {}
        context_dict['form'] = form
        return render(request, ('rango/yapper/user_profile_edit.html'), context=context_dict)



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
        breeds = Breed.objects.order_by("name")

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
def dog_profile(request, breed_name_slug, dog_slug):

    dprofile_context = {}

    try:
        breed   = Breed.objects.get(slug=breed_name_slug)
        dog     = Dog.objects.get(slug=dog_slug)
        participations = Participation.objects.filter(dog=dog)
       
        print(participations)
        dprofile_context['dog'] = dog
        dprofile_context['breed'] = breed
        dprofile_context['participations'] = participations

    except Dog.DoesNotExist:
        dprofile_context['dog'] = None
        dprofile_context['breed'] = None
        dprofile_context['participations'] = None

    return render(request, 'rango/yapper/dog_profile.html', dprofile_context)

# Add user_slug to args when /user/ is implemented
def add_dog(request):

    context_dict = {}

    form = AddDogForm()

    if request.method == 'POST':
        form = AddDogForm(request.POST)

        """Owner will be set in object once form is updated
        follows needs to be set in form as well sigh"""
        if form.is_valid():
            #username = request.user.get_username()
            #user = User.objects.get(username=username)
            #user_profile = UserProfile.objects.get(user=user)
            #dog = form.save(commit=False)
            #dog.owner = user_profile
            dog = form.save()
            # manually update slug + resave as auto increment dog_id occurs end of/post-save
            #dog.slug = slugify("{d.dog_id}-{d.name}".format(d=dog))
            #dog.save()

            breed = Breed.objects.get(name=dog.breed)
            print(breed.name)
            print(dog.name)
            print(dog.dog_id)
            print(dog.slug)

            return redirect(reverse('rango:dog_profile', kwargs={'breed_name_slug': breed.slug, 'dog_slug': dog.slug}))
        else:
            print(form.errors)  # This could be better done; for the purposes of TwD, this is fine. DM.
    
    context_dict = {'form': form}
    return render(request, 'rango/yapper/add_dog.html', context=context_dict)


def sports_homepage(request):
    
    # Context dictionary to input any external variables into the HTML template
    context_dict = {}
   
    sports_list = Sport.objects.order_by('name')
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
   
    competition_list = Competition.objects.order_by('date')
    context_dict['competitions'] = competition_list

    return render(request, 'rango/yapper/competition_homepage.html', context_dict)


def competition_profile(request, competition_name_slug):
    
    # Context dictionary to input any external variables into the HTML template
    context_dict = {}

    # Get the sport instance associated with the sport_name_slug
    try:
        competition = Competition.objects.get(slug=competition_name_slug)
        participation_list = Participation.objects.filter(competition=competition)
        
        print(participation_list)
        dog_list = list()
        for participation_item in participation_list:
            print(participation_item)
            print(participation_item.dog)
            dog_list.append(participation_item.dog)

        print(dog_list)

        breed_list = list()
        for dog_item in dog_list:
            print(dog_item.breed)
            breed_list.append(dog_item.breed)

        print(breed_list)
        context_dict['competition'] = competition
        context_dict['dogs'] = dog_list

    except Competition.DoesNotExist:
        context_dict['competition'] = None

    return render(request, 'rango/yapper/competition_profile.html', context_dict)

@login_required
def add_competition(request):

    form = CompetitionForm()

    if request.method == 'POST':
        
        # Get the form from the user POST 
        form = CompetitionForm(request.POST)

        # Check if the form is valid
        if form.is_valid():

            cleaned_data = form.cleaned_data

            # Get the sport from the form and then check if it exists 
            sport = cleaned_data["sport"]

            print(sport)
            if sport:
                competition = form.save(commit=False)
                competition.sport = sport
                competition.save()

                return redirect(reverse('rango:competitions', kwargs ={}))
        else:
            print(form.errors)  
    
    context_dict = {'form': form}
    return render(request, 'rango/yapper/add_competition.html', context=context_dict)

@login_required
def edit_competition(request, user_name_slug):
    
    form = CompetitionForm()

    if request.method == 'POST':
        
        # Get the form from the user POST 
        form = CompetitionForm(request.POST)

        # Check if the form is valid
        if form.is_valid():

            cleaned_data = form.cleaned_data

            # Get the sport from the form and then check if it exists 
            sport = cleaned_data["sport"]

            print(sport)
            if sport:
                competition = form.save(commit=False)
                competition.sport = sport
                competition.save()

                # Delete old
                #Competition.objects.filter(id=old_competition.id).delete()
                
                return redirect(reverse('rango:competitions', kwargs ={}))
        else:
            print(form.errors)  # This could be better done; for the purposes of TwD, this is fine. DM.
    
    context_dict = {'form': form}
    return render(request, 'rango/yapper/edit_competition.html', context=context_dict)

@login_required
def user_profile(request, user_name_slug):
    context_dict = {}
    try:
        user = UserProfile.objects.get(user_slug=user_name_slug)
        print(user, "in user profile view")
        context_dict['user_profile'] = user
        context_dict['followed_breeds']= user.followed_breeds
        context_dict['followed_sports']= user.followed_sports
        context_dict['followed_dogs']=user.followed_dogs
        context_dict['owned_dogs'] = user.owned_dogs
        context_dict['is_owner'] = user.is_owner
        context_dict['is_comp_org']= user.is_comp_org
        
        print(user.followed_breeds.all())
        print(user.followed_sports.all())
        print(user.followed_dogs.all())
    except UserProfile.DoesNotExist:
        (request, 'rango/yapper/user_profile.html',{})

    #dog_list = Dog.objects.filter(owner = user)
    
    return render(request, 'rango/yapper/user_profile.html', context=context_dict)

@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect(reverse('rango:index'))
    else:
        print(form.errors)

    context_dict = {'form': form}
    return render(request, 'rango/profile_registration.html', context_dict)



def faq(request):
    return render(request, 'rango/yapper/faq.html', {})

def explore(request):
    return render(request, 'rango/yapper/explore.html', {})


