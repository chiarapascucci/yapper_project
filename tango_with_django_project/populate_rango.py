import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page, Sport, Dog, Competition, Breed, Award, Participation

# For an explanation of what is going on here, please refer to the TwD book.

def populate():
<<<<<<< HEAD
  
=======
    
>>>>>>> main
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
                    'breed_restrictions': 'No cats allowed!!',
                    'follows': 100},
        'Running': {'competitions': running_competitions,
                    'description':'Running sport description',
                    'breed_restrictions': 'No cats allowed!!',
                    'follows': 200},
        'Sniffing': {'competitions': sniffing_competitions, 
                    'description':'Sniffing sport description',
                    'breed_restrictions': 'No cats allowed!!',
                    'follows': 300},
        'Pooing': {'competitions': pooing_competitions,
                    'description':'Pooing sport description',
                    'breed_restrictions': 'No cats allowed!!',
                    'follows': 1}}
    

<<<<<<< HEAD
    # Yapper popultation
    for sport_name, sport_data in sports.items():
        sport = add_sport(sport_name,sport_data['description'], sport_data['breed_restrictions'], sport_data['follows'])
        for c in sport_data['competitions']:
            print(type(c['description']))
            add_competition(sport, c['name'], c['description'], c['address'], c['location'], c['date'], c['eventpage'], c['isCompleted'])

=======
>>>>>>> main
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
    anaconda = {'name':'Anaconda',
            'breed':dachshund,}
    gareth = {'name': 'Gareth',
            'breed': irish_wolfhound}
    
    b = add_breed(bernese_mountain_dog["name"],bernese_mountain_dog["description"],1)
    print(b)
    b = add_breed(chow_chow["name"],chow_chow["description"])
    print(b)
    b = add_breed(dachshund["name"],dachshund["description"],2)
    d_anaconda = add_dog(anaconda["name"],b,3)
    print(b)
    print(d_anaconda)
    b = add_breed(irish_wolfhound["name"],irish_wolfhound["description"],2)
    d_gareth = add_dog(gareth['name'],b,10)
    print(b)
    b = add_breed(leonberger["name"],leonberger["description"],10)
    print(b)


    # Yapper popultation

    competitions = list()
    for sport_name, sport_data in sports.items():
        sport = add_sport(sport_name,sport_data['description'], sport_data['breed_restrictions'], sport_data['follows'])
        for c in sport_data['competitions']:
            competitions.append(add_competition(sport, c['name'], c['description'], c['address'], c['location'], c['date'], c['eventpage'], c['isCompleted']))


    # Populate the participation and awards
    awards = [         
        {'name':'Best girl',
         'description':'Best girl description',
         'certificate': None},
        {'name':'Best boy',
         'description':'Best boy description',
         'certificate': None},    
    ]

    print (competitions)
    participations = [
        {'name': 'p1',
        'dog': d_anaconda,
        'competition': competitions[0],
        'award': awards[0]},
        {'name': 'p2',
        'dog': d_gareth,
        'competition': competitions[1],
        'award': awards[1]}
    ]
    
    print (participations
    )
    for p_items in participations:
        award = add_award(p_items['award']['name'],p_items['award']['description'],p_items['award']['certificate'])
        participation = add_participation(p_items['name'],p_items['dog'], p_items['competition'], award)



# Add methods 

def add_breed(name, descrip, follows=0):
    b = Breed.objects.get_or_create(name=name)[0]
    b.description = descrip
    b.follows = follows
    print(b.follows)
    b.save()
    return b

# Add owner to this later
def add_dog(name, breed, follows=0):
    d = Dog.objects.get_or_create(name=name, breed=breed)[0]
    d.follows = follows
    d.save()
    return d


def add_sport(name, description, breed_restrictions, follows):
    s = Sport.objects.get_or_create(name=name)[0]
    s.description = description
    s.breed_restrictions = breed_restrictions
    s.follows = follows
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
    return co

def add_participation(name, dog, competition, award):

    # Set entity and relations 
    p = Participation.objects.get_or_create(name=name,dog=dog,competition=competition,award=award)[0]
    return p

def add_award(name, description, certificate):

    # Set entity
    a = Award.objects.get_or_create(name=name)[0]

    a.description = description
    a.certificate = certificate
    return a



# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()