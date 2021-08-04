import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page, Sport, Dog, Competition, Breed, Award, Participation

# For an explanation of what is going on here, please refer to the TwD book.

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/',
         'views': 114,},
        {'title':'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/',
         'views': 53},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/',
         'views': 20} ]
    
    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 32},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/',
         'views': 12},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/',
         'views': 1258} ]
    
    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/',
         'views': 54},
        {'title':'Flask',
         'url':'http://flask.pocoo.org',
         'views': 64} ]
    
    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16} }

    # Yapper population

    jumping_competitions = [ 
        {'name':'Comp A',
         'description':'Comp A description',
         'address': 'Address A',
         'location': None,
         'date': None,
         'eventpage': None,
         'isCompleted': False},
        {'name':'Comp B',
         'description':'Comp B description',
         'address': 'Address B',
         'location': None,
         'date': 0,
         'eventpage': None,
         'isCompleted': False},
        {'name':'Comp C',
         'description':'Comp C description',
         'address': 'Address C',
         'location': None,
         'date': 0,
         'eventpage': None,
         'isCompleted': False},
    ]

    running_competitions = [
        {'name':'Comp D',
         'description':'Comp D description',
         'address': 'Address D',
         'location': None,
         'date': 0,
         'eventpage': None,
         'isCompleted': False},
        {'name':'Comp E',
         'description':'Comp E description',
         'address': 'Address E',
         'location': None,
         'date': 0,
         'eventpage': None,
         'isCompleted': False},
    ]

    sniffing_competitions = [
        {'name':'Comp F',
         'description':'Comp F description',
         'address': 'Address F',
         'location': None,
         'date': 0,
         'eventpage': None,
         'isCompleted': False},       
    ]

    pooing_competitions = [
        {'name':'Comp G',
         'description':'Comp G description',
         'address': 'Address G',
         'location': None,
         'date': 0,
         'eventpage': None,
         'isCompleted': False}, 
    ]


    sports = {'Jumping': {'competitions': jumping_competitions, 
                    'description':'Jumping sport description',
                    'breed_restrictions': 'No cats allowed!!'},
        'Running': {'competitions': running_competitions,
                    'description':'Running sport description',
                    'breed_restrictions': 'No cats allowed!!'},
        'Sniffing': {'competitions': sniffing_competitions, 
                    'description':'Sniffing sport description',
                    'breed_restrictions': 'No cats allowed!!'},
        'Pooing': {'competitions': pooing_competitions,
                    'description':'Pooing sport description',
                    'breed_restrictions': 'No cats allowed!!'}}
    

    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views=p['views'])


    # Yapper popultation
    for sport_name, sport_data in sports.items():
        sport = add_sport(sport_name,sport_data['description'], sport_data['breed_restrictions'])
        for c in sport_data['competitions']:
            print(type(c['description']))
            add_competition(sport, c['name'], c['description'], c['address'], c['location'], c['date'], c['eventpage'], c['isCompleted'])

    # Dog & Breed population
    # Messy version for testing purposes for now

    bernese_mountain_dog = {'name':'Bernese Mountain Dog',
                            'description':'Descrip A',}
    chow_chow = {'name':'Chow Chow',
            'description':'Descrip B',}
    dachshund = {'name':'Dachshund',
            'description':'Descrip C',}
    irish_wolfhound = {'name':'Irish Wolfhound',
            'description':'Descrip D',}
    leonberger = {'name':'Leonberger',
                'description':'Descrip E',}

    # Dogs
    anaconda = {'name':'anaconda',
            'breed':dachshund,}
    
    b = add_breed(bernese_mountain_dog["name"],bernese_mountain_dog["description"])
    print(b)
    b = add_breed(chow_chow["name"],chow_chow["description"])
    print(b)
    b = add_breed(dachshund["name"],dachshund["description"])
    d = add_dog(anaconda["name"],b)
    print(b)
    print(d)
    b = add_breed(irish_wolfhound["name"],irish_wolfhound["description"])
    print(b)
    b = add_breed(leonberger["name"],leonberger["description"])
    print(b)


# Add methods 
def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c



def add_breed(name, descrip):
    b = Breed.objects.get_or_create(name=name)[0]
    b.description = descrip
    b.save()
    return b

# Add owner to this later
def add_dog(name, breed):
    d = Dog.objects.get_or_create(name=name, breed=breed)[0]
    d.save()
    return d

    

def add_sport(name, description, breed_restrictions):
    s = Sport.objects.get_or_create(name=name)[0]
    s.description = description
    s.breed_restrictions = breed_restrictions
    s.save()
    return s

def add_competition(sport, name, description, address, location, date, eventpage, isCompleted):
    
    # Set entity relation 
    co = Competition.objects.get_or_create(sport=sport, name=name)[0]

    # Set attributes
    co.description = description
    co.address = address
    co.location = location
    co.date = date
    co.eventpage = eventpage
    co.isCompleted = isCompleted




# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()