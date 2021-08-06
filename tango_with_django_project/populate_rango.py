import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Sport, Dog, Competition, Breed, Award, Participation, User, UserProfile
import datetime
import random as rand
from django.contrib.auth.hashers import PBKDF2PasswordHasher, make_password

# For an explanation of what is going on here, please refer to the TwD book.

def populate():
  
    ############### data dictionaries ############################

    # Yapper population

    ###COMPETITIONS####
    agility_competitions = [ 
        {'name':'Glasgow Agility competition',
         'description':"Competition where dogs test their mettle vs other dogs in Glasgow",
         'address': "University of Glasgow, Glasgow G12 8QQ, UK",
         'location': None,
         'date': datetime.date(2021,9,2),
         'eventpage': 'https://en.wikipedia.org/wiki/Dog_agility',
         'isCompleted': False},
        {'name':'Edinburgh Agility competition',
         'description':'Comp B description',
         'address': 'Old College, South Bridge, Edinburgh EH8 9YL, UK',
         'location': None,
         'date': datetime.date(2021,10,9),
         'eventpage': 'https://en.wikipedia.org/wiki/Dog_agility',
         'isCompleted': False},
        {'name':'Aberdeen Agility competition',
         'description':'Comp C description',
         'address': "King's College, Aberdeen AB24 3FX, UK",
         'location': None,
         'date': datetime.date(2021,8,22),
         'eventpage': 'https://en.wikipedia.org/wiki/Dog_agility',
         'isCompleted': False},
    ]

    earthdogtrials_competitions = [
        {'name':'Earthdigging Dogs competition',
         'description':'Comp D description',
         'address': "King's College, Aberdeen AB24 3FX, UK",
         'location': None,
         'date': datetime.date(2021,10,22),
         'eventpage': 'https://en.wikipedia.org/wiki/Earthdog_trial',
         'isCompleted': False},
        {'name':'Edinburgh Earthdog trials (not by combat)',
         'description':'Comp E description',
         'address': 'Old College, South Bridge, Edinburgh EH8 9YL, UK',
         'location': None,
         'date': datetime.date(2021,12,2),
         'eventpage': 'https://en.wikipedia.org/wiki/Earthdog_trial',
         'isCompleted': False},
    ]

    flyball_competitions = [
        {'name':'Finneston Flyball competition',
         'description':'Comp F description',
         'address': '16 Richmond St, Glasgow G1 1XQ, UK',
         'location': None,
         'date': datetime.date(2021,5,29),
         'eventpage': 'https://en.wikipedia.org/wiki/Flyball',
         'isCompleted': True},  
        {'name':'Is it a bird? Is it a plane? No its a ball',
         'description':'Comp F description',
         'address': '16 Richmond St, Glasgow G1 1XQ, UK',
         'location': None,
         'date': datetime.date(2021,12,29),
         'eventpage': 'https://en.wikipedia.org/wiki/Flyball',
         'isCompleted': False},       
    ]

    herding_competitions = [
        {'name':'Herding the herd competition',
         'description':'Comp G description',
         'address': 'Old College, South Bridge, Edinburgh EH8 9YL, UK',
         'location': None,
         'date': datetime.date(2021,3,2),
         'eventpage': 'https://en.wikipedia.org/wiki/Herding',
         'isCompleted': True}, 
        {'name':'I Herd you like Herding dogs',
         'description':'Comp G description',
         'address': 'Old College, South Bridge, Edinburgh EH8 9YL, UK',
         'location': None,
         'date': datetime.date(2021,11,20),
         'eventpage': 'https://en.wikipedia.org/wiki/Herding',
         'isCompleted': False}, 
        {'name':'Hamilton Herding competition',
         'description':'Comp G description',
         'address': '16 Richmond St, Glasgow G1 1XQ, UK',
         'location': None,
         'date': datetime.date(2021,10,30),
         'eventpage': 'https://en.wikipedia.org/wiki/Herding',
         'isCompleted': False}, 
    ]

    dockdiving_competitions = [
        {'name':'Dundee Dog Diving Docks competition',
         'description':'Comp G description',
         'address': "King's College, Aberdeen AB24 3FX, UK",
         'location': None,
         'date': datetime.date(2021,3,2),
         'eventpage': 'https://en.wikipedia.org/wiki/Dock_jumping',
         'isCompleted': True}, 
         {'name':'Dabbing diving dogs at the Docks',
         'description':'Comp G description',
         'address': "King's College, Aberdeen AB24 3FX, UK",
         'location': None,
         'date': datetime.date(2021,10,20),
         'eventpage': 'https://en.wikipedia.org/wiki/Dock_jumping',
         'isCompleted': False}, 
    ]

    ###SPORTS####

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
                    'follows': 400},
        'Dock diving':  {'competitions': dockdiving_competitions,
                    'description':"Dock Diving is a relatively new sport that has dogs jumping and splashing! It first appeared as an organized canine sport in 2007 and has since exploded. This is an amazing sport for dogs that love to fetch, swim, or both and titles are offered to any breed or mixed breed. The UKC began giving Dock Diving titles in 2009; the AKC in 2014. It takes place on a stationary 35’ to 40’ (11-12m) dock that is placed over a pool that is about 8’ (2.5m) long and at least 4’ (1.2m) deep.",
                    'breed_restrictions': 'No restrictions.',
                    'follows': 250}}

    ###BREEDS###

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

    ###DOGS###
    
    anaconda = {'name':'Anaconda',
            'breed':dachshund,}
    fluffy = {'name':'Mr Fluffykins VI',
            'breed':dachshund,}
    dog1 =   {'name':'dogge',
            'breed':dachshund,},
    dog2  = {'name':'doggy',
            'breed':dachshund,}
    
    ###LIST OF DOGS PER BREED ###
    bernese_dogs = [
        {'name': 'anaconda'},
        {'name': 'Berni'},
        {'name': 'Bongo'},
    ]
    chowchow_dogs = [
        {'name': 'Congo'},
        {'name': 'Cassandra'},
        {'name': 'Dog'},
    ]
    dachshund_dogs = [
        {'name': 'Darshan'},
        {'name': 'Dana'},
        {'name': 'Zander'},
    ]
    irish_wolf_dogs = [ 
        {'name': 'Welma'},
        {'name': 'Chan'},
        {'name': 'Barnie'},
    ]
    leonberger_dogs = [ 
        {'name': 'Morag'},
        {'name': 'Molly'},
        {'name': 'Fetch'},
        {'name': 'Brodie'},
    ]
    greyhound_dogs = [
        {'name': 'Polly'},
        {'name': 'Ban'},
        {'name': 'Plop'},
    ]
    scottish_deerhound_dogs = [
        {'name': 'Billy'},
        {'name': 'Fido'},
        {'name': 'Dash'},
        {'name': 'Gareth'},
    ]
    cocker_spaniel_dogs= [
        {'name': 'Jilly'},
        {'name': 'Luke Skywalker'},
        {'name': 'Sauron'},
    ]
    german_shepherd_dogs = [
        {'name': 'Loki'},
        {'name': 'Thor'},
        {'name': 'Siegfried'},
        {'name': 'Olaf'},
    ]
    shetland_sheepdogs = [
        {'name': 'Seamus'},
        {'name': 'Yona'},
        {'name': 'Shona'},
        {'name': 'Harry Potter'},
    ]
    siberian_husky_dogs = [
        {'name': 'Vladamir'},
        {'name': 'Sputnik'},
        {'name': 'Paul'},
    ]
    malmute_dogs = [
        {'name': 'Malmo'},
        {'name': 'Malmi'},
        {'name': 'Malma'},
    ]

    breeds = [
        {'name':'Bernese Mountain Dog',
        'description':"The Bernese Mountain Dog (German: Berner Sennenhund) is a large dog breed, one of the four breeds of Sennenhund-type dogs from the Swiss Alps. These dogs have roots in the Roman mastiffs. The name Sennenhund is derived from the German Senne (alpine pasture) and Hund (hound/dog), as they accompanied the alpine herders and dairymen called Senn. Berner (or Bernese in English) refers to the area of the breed's origin, in the canton of Bern. This breed was originally kept as a general farm dog. Large Sennenhunde in the past were also used as draft animals, pulling carts. The breed was officially established in 1912.",
        'dogs': bernese_dogs},
        {'name':'Chow Chow',
        'description':"The Chow Chow is a dog breed originally from northern China. The Chow Chow is a sturdily built dog, square in profile, with a broad skull and small, triangular, erect ears with rounded tips. The breed is known for a very dense double coat that is either smooth or rough. The fur is particularly thick in the neck area, giving it a distinctive ruff or mane appearance. The coat may be shaded/self-red, black, blue, cinnamon/fawn, or cream.",
        'dogs': chowchow_dogs},
        {'name':'Dachshund',
        'description':"The dachshund (German: badger dog), also known as the wiener dog, badger dog, sausage dog, is a short-legged, long-bodied, hound-type dog breed. They may be smooth, wire, or long-haired. The standard-sized dachshund was developed to scent, chase, and flush out badgers and other burrow-dwelling animals, while the miniature dachshund was bred to hunt small animals such as rabbits and other smaller animal",
        'dogs': dachshund_dogs},
        {'name':'Irish Wolfhound',
        'description':"The Irish Wolfhound is a historic sighthound dog breed from Ireland that has, by its presence and substantial size, inspired literature, poetry and mythology.Like all sighthounds, it was used to pursue game by speed; it was also famed as a guardian dog, specializing in protection against and for the hunting of wolves. The original dog-type was presumed extinct by most knowledgeable authors but recreated specifically for the canine fancy mainly by Captain George A. Graham in the late 19th century.The modern breed, classified by recent genetic research into the Sighthound United Kingdom Rural Clade has been used by coursing hunters who have prized it for its ability to dispatch game caught by other, swifter sighthounds",
        'dogs': irish_wolf_dogs},
        {'name':'Leonberger',
        'description':"The Leonberger is a dog breed, whose name derives from the city of Leonberg in Baden-Württemberg, Germany.This breed occurs with a generous double coat; the Leonberger is a large, muscular, and elegant dog with balanced body type, medium temperament, and dramatic presence. The head is adorned with a striking black mask and projects the breed's distinct expression of intelligence, pride, and kindliness. Remaining true to their early roots as a capable family and working dog and search-and-rescue dog (particularly water), the surprisingly agile Leonberger is sound and coordinated, with both strength in bearing and elegance in movement. A sexually dimorphic breed, the Leonberger possesses either a strongly masculine or elegantly feminine form, making gender immediately discernible.",
        'dogs': leonberger_dogs},
        {'name': 'Scottish Deerhound',
        'description': "The Scottish Deerhound, or simply the Deerhound, is a large breed of hound (a sighthound), once bred to hunt the red deer by coursing. In outward appearance, the Scottish Deerhound is similar to the Greyhound, but larger and more heavily boned with a rough-coat. The Deerhound is closely related to the Irish Wolfhound and was a contributor to that breed when it was re-created at the end of the 19th century.",
        'dogs': scottish_deerhound_dogs},
        {'name': 'Cocker Spaniel',
        'description': "Cocker Spaniels are dogs belonging to two breeds of the spaniel dog type: the American Cocker Spaniel and the English Cocker Spaniel, both of which are commonly called simply Cocker Spaniel in their countries of origin. In the early 20th century, Cocker Spaniels also included small hunting spaniels. Cocker Spaniels were originally bred as hunting dogs in the United Kingdom, with the term 'cocker' deriving from their use to hunt the Eurasian woodcock. When the breed was brought to the United States, it was bred to a different standard, which enabled it to specialize in hunting the American woodcock. Further physical changes were bred into the cocker in the United States during the early part of the 20th century.",
        'dogs': cocker_spaniel_dogs},
        {'name': 'German Shepherd',
        'description': "The German Shepherd is a breed of medium to large-sized working dog that originated in Germany. According to the FCI, the breed's English language name is German Shepherd Dog. The breed was officially known as the Alsatian Wolf Dog in the UK from after the First World War until 1977 when its name was changed back to German Shepherd. Despite its wolf-like appearance, the German Shepherd is a relatively modern breed of dog, with its origin dating to 1899. As a herding dog, German Shepherds are working dogs developed originally for herding sheep. Since that time, however, because of their strength, intelligence, trainability, and obedience, German Shepherds around the world are often the preferred breed for many types of work, including disability assistance, search-and-rescue, police and military roles and acting. The German Shepherd is the second-most registered breed by the American Kennel Club and seventh-most registered breed by The Kennel Club in the United Kingdom",
        'dogs': german_shepherd_dogs},
        {'name': 'Greyhound',
        'description': "The Greyhound is a breed of dog, a sighthound which has been bred for coursing game and greyhound racing. It is also referred to as an English Greyhound. Since the rise in large-scale adoption of retired racing Greyhounds, the breed has seen a resurgence in popularity as a family pet. According to Merriam-Webster, a Greyhound is any of a breed of tall slender graceful smooth-coated dogs characterized by swiftness and keen sight, as well as any of several related dogs, such as the Italian Greyhound. The Greyhound is a gentle and intelligent breed whose combination of long, powerful legs, deep chest, flexible spine, and slim build allows it to reach average race speeds exceeding 64 kilometres per hour (40 mph). The Greyhound can reach a full speed of 70 kilometres per hour (43 mph) within 30 metres (98 ft), or six strides from the boxes, traveling at almost 20 metres per second (66 ft/s) for the first 250 metres (820 ft) of a race.",
        'dogs': greyhound_dogs},
        {'name': 'Shetland Sheepdog',
        'description': "The Shetland Sheepdog, often known as the Sheltie, is a breed of herding dog that originated in the Shetland Islands of Scotland. The original name was Shetland Collie, but this caused controversy amongst Rough Collie breeders of the time, so the breed's name was formally changed. This diligent small dog is clever, vocal, excitable and willing to please. They are incredibly trustworthy to their owners to the point where they are often referred to as shadows due to their attachment to family. This breed was formally recognized by The Kennel Club (UK) in 1909. Like the Shetland pony, Shetland cattle and the Shetland sheep, the Shetland Sheepdog is a hardy but diminutive breed developed to thrive amidst the harsh and meagre conditions of its native islands. While the Sheltie still excels at herding, today it is often raised as a working dog and/or family pet.",
        'dogs': shetland_sheepdogs},
        {'name': 'Siberian Husky',
        'description': "The Siberian Husky is a medium-sized working sled dog breed. The breed belongs to the Spitz genetic family. It is recognizable by its thickly furred double coat, erect triangular ears, and distinctive markings, and is smaller than the similar-looking Alaskan Malamute. Siberian Huskies originated in Northeast Asia where they are bred by the Chukchi people of Siberia for sled pulling, and companionship.It is an active, energetic, resilient breed, whose ancestors lived in the extremely cold and harsh environment of the Siberian Arctic. William Goosak, a Russian fur trader, introduced them to Nome, Alaska, during the Nome Gold Rush, initially as sled dogs to work the mining fields and for expeditions through otherwise impassable terrain. Today, the Siberian Husky is typically kept as a house pet, though they are still frequently used as sled dogs by competitive and recreational mushers",
        'dogs': siberian_husky_dogs},
        {'name': 'Alaskan Malamute',
        'description': "The Alaskan Malamute is a large breed of dog that was originally bred for their strength and endurance to haul heavy freight as a sled dog and hound.They are similar to other arctic, husky, and spitz breeds such as the Greenland Dog, Canadian Eskimo Dog, the Siberian Husky, and the Samoyed.",
        'dogs': malmute_dogs},
    ]

    ###AWARDS###

    awards = [         
        {'name':'Best girl',
         'description':'Best girl description',
         'certificate': None},
        {'name':'Best boy',
         'description':'Best boy description',
         'certificate': None},    
    ]

    ###USERS AND USER PROFILES###

    users = {
       'chp': {'username' : 'chp', 'email':'g1@mail.com', 'password': 'helloyou123'},
       'chpa': {'username' : 'chpa', 'email':'g2@mail.com', 'password': 'helloyou123'},
       'chpas' : {'username' : 'chpas', 'email':'g3@mail.com', 'password': 'helloyou123'},
        'chpi': {'username' : 'chpi', 'email':'g4@mail.com', 'password': 'helloyou123'},
        'chpic' : {'username' : 'chpic', 'email':'g5@mail.com', 'password': 'helloyou123'},
    }

    user_profile = {
        '111':{'id':'111', 'followed_dogs': [dog1, dog2], 'followed_breeds': [chow_chow, bernese_mountain_dog], 'followed_sports' : sports['Agility'], 
        'bio':'I am awesome', 'user_slug' : 'chp', 'owned_dogs' : anaconda, 'is_owner' : True, 'is_comp_org': False },
        '22':{'id':'22', 'followed_dogs': [dog1, fluffy, dog2], 'followed_breeds': [chow_chow, bernese_mountain_dog], 'followed_sports' : sports['Herding'], 
        'bio':'I am awesome', 'user_slug' : 'chpa', 'is_owner' : False, 'is_comp_org': False },
        '3232':{'id':'3232', 'followed_dogs': [anaconda, dog2], 'followed_breeds': [dachshund, chow_chow, leonberger], 'followed_sports' : sports['Flyball'], 
        'bio':'I am awesome', 'user_slug' : 'chpas', 'is_owner' : False, 'is_comp_org': False },
        '3434':{'id':'3434', 'followed_dogs': [fluffy, dog1], 'followed_breeds': [dachshund, chow_chow, leonberger], 'followed_sports' : sports['Agility'], 
        'bio':'I am awesome', 'user_slug' : 'chpi', 'owned_dogs': fluffy, 'is_owner' : True, 'is_comp_org': False },
        '254':{'id':'254', 'followed_dogs': [anaconda, dog1], 'followed_breeds': [dachshund, chow_chow, leonberger], 'followed_sports' : sports['Agility'], 
        'bio':'I am awesome', 'user_slug' : 'chpic', 'owned_dogs': [dog1, dog2], 'is_owner' : True, 'is_comp_org': False },
    }

    ################ SCRIPT POPULATION LOGIC #########################
    
    ###SPORTS###

    for sport_name, sport_data in sports.items():
        sport = add_sport(sport_name,sport_data['description'], sport_data['breed_restrictions'], sport_data['follows'])
        for c in sport_data['competitions']:
            add_competition(sport, c['name'], c['description'], c['address'], c['location'], c['date'], c['eventpage'], c['isCompleted'])

    # competition list for easy future refernce in setting Participation entities 
    competitions = list()
    sport_list = []

    # Populate sports and competitions with population data
    for sport_name, sport_data in sports.items():
        sport = add_sport(sport_name,sport_data['description'], sport_data['breed_restrictions'], sport_data['follows'])
        sport_list.append(sport)
        for c in sport_data['competitions']:
            competitions.append(add_competition(sport, c['name'], c['description'], c['address'], c['location'], c['date'], c['eventpage'], c['isCompleted']))


    # Populate Breeds and dogs
    dog_list = list()
    breed_list =[]
    for breed_data in breeds:
        breed = add_breed(breed_data['name'],breed_data['description'], rand.randint(0,10000))
        breed_list.append(breed)
        for dog_data in breed_data['dogs']:
            dog = add_dog(dog_data['name'], breed,rand.randint(0,1000))
            dog_list.append(dog)

    # Populate the participation and awards
    # Participation list which is filled with participation information for each dog
    participation_list = list()
    i = 0
    for dog in dog_list:

        # Dictionary of participation informaition which is populated with a random competition and reward
        participation_structure = {} 

        # Get a random competition to set the dog in
        randCompetition = competitions[rand.randint(0,len(competitions)-1)]

        # Check if its complete, if so then give a random award for now..
        if randCompetition.isCompleted:
            participation_structure = {
            'name': str(i),
            'dog': dog,
            'competition': randCompetition,
            'award': awards[rand.randint(0,len(awards)-1)]}
        else:
            participation_structure = {
            'name': str(i),
            'dog': dog,
            'competition': randCompetition,
            'award': None}

        participation_list.append(participation_structure)
        i = i + 1

    # Create entities of Awards and Participation
    # Reset awards as repopulating and using create to generate them since want an Award per Participation 
    # (using only two unique award structures so need to make duplicates)
    Award.objects.all().delete()

    for p_items in participation_list:
        
        # Add an award (None if none) and participation
        if p_items['award'] != None:
            award = add_award(p_items['award']['name'], p_items['award']['description'],p_items['award']['certificate'])
            participation = add_participation(p_items['name'],p_items['dog'], p_items['competition'], award)
        else:
            participation = add_participation(p_items['name'],p_items['dog'], p_items['competition'], None)

   
    
    b = add_breed(bernese_mountain_dog["name"],bernese_mountain_dog["description"],1)
    print(b)
    b = add_breed(chow_chow["name"],chow_chow["description"])
    print(b)
    b = add_breed(dachshund["name"],dachshund["description"],2)
    # Add owner to args
    d = add_dog(anaconda["name"],b,9001)
    print(b)
    print(d)
    d = add_dog(fluffy["name"],b,8999)
    print(b)
    print(d)
    b = add_breed(irish_wolfhound["name"],irish_wolfhound["description"],2)
    print(b)
    b = add_breed(leonberger["name"],leonberger["description"],10)
    print(b)

    ##USER PROFILES###
    
    user_list = []
    
    for username, user_data in users.items():
        user = create_user(username, user_data['email'], user_data['password'])
        print("creating: ", user.username)
        user_list.append(user)
    
    user_list.reverse()

    i=0
    print(i)

    user_profile_list = []
    for id, user_profile_data in user_profile.items():
        user_profile = create_userprofile(user_list[i], user_profile_data['bio'], user_profile_data['user_slug'], user_profile_data['is_owner'], user_profile_data['is_comp_org'])
        print("creating: ", user_profile.user_slug, ", i: ", i)
        user_profile_list.append(user_profile)
        i = i+1
        if i==5:
            break

    print(len(dog_list))
    d = dog_list[0]
    print(d)
    #user_profile_list[0].followed_dogs.add(d)

    for dog in dog_list:
        i=rand.randint(0,4)
        print(i)
        user_profile_list[i].followed_dogs.add(dog)
        user_profile_list[i].save()
        print(user_profile_list[i], " dog ", dog)

    for sport in sport_list:
        i=rand.randint(0,4)
        print(i)
        user_profile_list[i].followed_sports.add(sport)
        user_profile_list[i].save()
        print(user_profile_list[i], " sport ", sport)

    for breed in breed_list:
        i=rand.randint(0,4)
        print(i)
        user_profile_list[i].followed_breeds.add(breed)
        user_profile_list[i].save()
        print(user_profile_list[i], " breed ", breed)



    #user_profile_list[1].followed_dogs.add(dog_list[10:20])
    #user_profile_list[2].followed_dogs.add(dog_list[20:39])



   

###############HELPER METHODS##########################
def create_user(username, email, password):
    user = User.objects.get_or_create(username=username)[0]
    user.email = email
    user.password = make_password(password, salt=None, hasher='default')
    user.save()
    return user

def create_userprofile(user, bio, user_slug, is_owner, is_comp_org):
    print("call to method")
    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    user_profile.bio = bio
    user_profile.user_slug = user_slug
    user_profile.is_owner = is_owner
    user_profile.is_comp_org = is_comp_org
    user_profile.save()
    return user_profile



def add_breed(name, descrip, follows=0):
    b = Breed.objects.get_or_create(name=name)[0]
    b.description = descrip
    b.follows = follows
    b.save()
    return b



# Add owner to args when implemented
def add_dog(name, breed, follows=0):
    d = Dog.objects.get_or_create(name=name, breed=breed)[0]
    d.follows = follows
    #d.owner = owner
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
    co.save()
    return co

def add_participation(name, dog, competition, award):

    # Set entity and relations 
    p = Participation.objects.get_or_create(name=name,dog=dog,competition=competition,award=award)[0]
    p.save()
    return p

def add_award(name, description, certificate):

    # Set entity (using create here as in a 1-1 relation and dont want to violate unique constraint)
    a = Award.objects.create()

    a.name = name
    a.description = description
    a.certificate = certificate
    a.save()
    return a


# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()