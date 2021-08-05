import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page, Sport, Dog, Competition, Breed, Award, Participation
import datetime

# For an explanation of what is going on here, please refer to the TwD book.

def populate():
  
    
    # Yapper population
    agility_competitions = [ 
        {'name':'Glasgow Agility competition',
         'description':"Comp A description",
         'address': "Address A",
         'location': None,
         'date': datetime.date(2021,9,2),
         'eventpage': None,
         'isCompleted': False},
        {'name':'Edinburgh Agility competition',
         'description':'Comp B description',
         'address': 'Address B',
         'location': None,
         'date': datetime.date(2021,10,9),
         'eventpage': None,
         'isCompleted': False},
        {'name':'Aberdeen Agility competition',
         'description':'Comp C description',
         'address': 'Address C',
         'location': None,
         'date': datetime.date(2021,8,22),
         'eventpage': None,
         'isCompleted': False},
    ]

    earthdogtrials_competitions = [
        {'name':'Earth doggo compo competition',
         'description':'Comp D description',
         'address': 'Address D',
         'location': None,
         'date': datetime.date(2021,10,22),
         'eventpage': None,
         'isCompleted': False},
        {'name':'Edinburgh Earthdog trials (not by combat)',
         'description':'Comp E description',
         'address': 'Address E',
         'location': None,
         'date': datetime.date(2021,12,2),
         'eventpage': None,
         'isCompleted': False},
    ]

    flyball_competitions = [
        {'name':'Is it a bird? Is it a plane? No its a ball',
         'description':'Comp F description',
         'address': 'Address F',
         'location': None,
         'date': datetime.date(2021,3,2),
         'eventpage': None,
         'isCompleted': False},       
    ]

    herding_competitions = [
        {'name':'I Herd you like Herding dogs',
         'description':'Comp G description',
         'address': 'Address G',
         'location': None,
         'date': datetime.date(2021,3,2),
         'eventpage': None,
         'isCompleted': False}, 
        {'name':'Hamilton Herding competition',
         'description':'Comp G description',
         'address': 'Address G',
         'location': None,
         'date': datetime.date(2021,3,2),
         'eventpage': None,
         'isCompleted': False}, 
    ]

    dockdiving_competitions = [
        {'name':'Dabbing diving dogs at the Docks',
         'description':'Comp G description',
         'address': 'Address G',
         'location': None,
         'date': datetime.date(2021,3,2),
         'eventpage': None,
         'isCompleted': False}, 
    ]


    sports = {'Agility': {'competitions': agility_competitions, 
                    'description':"Agility is a dog sport in which the handler directs the dog over a series of obstacles using only voice and body signals. It’s a race against the clock and the fastest dog (without any penalties) wins. The handler cannot use toys or food as incentives during a competition, only voice and body signals. Agility requires exceptional training of the dog",
                    'breed_restrictions': "No restrictions.",
                    'follows': 100},
        'Earthdog trials': {'competitions': earthdogtrials_competitions,
                    'description':"Earthdog Trials is a competition mainly involving terriers. In a trial, a long tunnel is dug underground and a scent trail is laid, to make the course simulate a real animal den. Typically a rat or a similar animal is placed at the end of the tunnel in a cage. The dog involved in the trial is placed at the entrance to the burrow, and is released on a signal. The dog then navigates the tunnel, following the scent trail underground and finding the animal. The dog then “flushes” the animal by barking at it to try to make it escape so that, in theory, the hunter can shoot it. This is called working the quarry. The quarry in this case is the animal",
                    'breed_restrictions': "Allowed breeds: - .... ",
                    'follows': 200},
        'Flyball': {'competitions': flyball_competitions, 
                    'description':"Flyball is a dog sport in which teams of dogs race over a line of four small jumps to a box which releases a tennis ball when the dog presses the spring. The dog has to catch the ball when it is fired into the air by the box. The dog then races back over the jumps to its handler while carrying the ball. The next handler then lets his or her dog go, and the process is repeated until every team member has completed the run. Flyball is effectively a relay sport.",
                    'breed_restrictions': "No restrictions.",
                    'follows': 300},
        'Herding': {'competitions': herding_competitions,
                    'description':"Herding competitions are often called herding trials. In these trials, dogs have to move sheep around a field, often through gates, fences, and into and out of enclosures as directed by their handlers. Some trials contain a pair of dogs being used, called a “brace,” while others involve only one dog. Trials like these have been around for hundreds of years.",
                    'breed_restrictions': "Herding breed dogs.",
                    'follows': 1},
        'Dock diving':  {'competitions': dockdiving_competitions,
                    'description':"Dock Diving is a relatively new sport that has dogs jumping and splashing! It first appeared as an organized canine sport in 2007 and has since exploded. This is an amazing sport for dogs that love to fetch, swim, or both and titles are offered to any breed or mixed breed. The UKC began giving Dock Diving titles in 2009; the AKC in 2014. It takes place on a stationary 35’ to 40’ (11-12m) dock that is placed over a pool that is about 8’ (2.5m) long and at least 4’ (1.2m) deep.",
                    'breed_restrictions': 'No restrictions.',
                    'follows': 1}}

    # Yapper popultation
    for sport_name, sport_data in sports.items():
        sport = add_sport(sport_name,sport_data['description'], sport_data['breed_restrictions'], sport_data['follows'])
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

    print(type(date))
    # Set attributes
    co.description = description
    co.address = address
    co.location = location
    co.date = date
    print(co.date)
    co.eventpage = eventpage
    co.isCompleted = isCompleted
    co.save()
    return co

def add_participation(name, dog, competition, award):

    # Set entity and relations 
    p = Participation.objects.get_or_create(name=name,dog=dog,competition=competition,award=award)[0]
    p.save()
    return p

def add_award(name, description, certificate):

    # Set entity
    a = Award.objects.get_or_create(name=name)[0]

    a.description = description
    a.certificate = certificate
    a.save()
    return a



# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()