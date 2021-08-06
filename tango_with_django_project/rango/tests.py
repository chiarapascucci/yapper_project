from django.test import TestCase
from django.test import Client
from rango.models import Sport, Dog, Competition, Breed, Award, Participation, User, UserProfile
from django.urls import reverse, resolve
import random as rand
import datetime
import os
import inspect
from django.contrib.auth.hashers import PBKDF2PasswordHasher, make_password


# Create your tests here.

class ModelUnitTests(TestCase):

    def setUp(self):
        

        # Instantiate differnt entites and populate  
        # Sport entity 
        sport = Sport.objects.create(name="football")
        sport.slug = sport.name
        sport.save()

        # Competition entity
        competition = Competition.objects.create(name="competition",sport=sport)
        competition.address = "address"
        competition.date = datetime.date(2021,10,22)
        competition.eventpage = "http:/www.youtube.com"
        competition.slug = competition.name
        competition.save()

        # Breed emtity
        breed = Breed.objects.create(name="malamute")
        breed.description = "description"
        breed.follows = 20
        breed.slug = breed.name
        breed.save()

        # Dog entity
        dog = Dog.objects.create(name="doggo", breed=breed)
        dog.main_about = "description"
        dog.follows = 30
        dog.slug = dog.name
        dog.save()

        # Award entity
        award = Award.objects.create(name="thebest")
        award.description = "description"
        award.certificate_path = "pathtofglory"
        award.save()

        # Participation entity
        participation = Participation.objects.create(name = "participation", dog=dog, competition=competition, award=award)

        # User entity
        user = User.objects.get_or_create(username="bob")[0]
        user.email = 'g4@mail.com'
        user.password = make_password("workplease123", salt=None, hasher='default')
        user.save()


    def test_ModelAttributeRetrieval(self):

        print("Testing model relations and values:\n\n")
        
        # Fetch entities
        print("\nT1: Testing object retrieval from SQLite DB - ")
        sport = Sport.objects.get(name="football")
        competition = Competition.objects.get(name="competition")
        breed = Breed.objects.get(name="malamute")
        dog = Dog.objects.get(name="doggo")
        award = Award.objects.get(name="thebest")
        participation = Participation.objects.get(name="participation")

        self.assertIsNotNone(sport,         'Sport does not exist.')
        self.assertIsNotNone(competition,   'Competition does not exist.')
        self.assertIsNotNone(breed,         'Breed does not exist.')
        self.assertIsNotNone(dog,           'Dog does not exist.')
        self.assertIsNotNone(award,         'Award does not exist.')
        self.assertIsNotNone(participation, 'Participation does not exist.')
        print("All passed.")


    def test_ModelRelations(self):

        print("\nT2: Testing model relationships - ")
        # Retrieve objects again (fine from first test)
        sport = Sport.objects.get(name="football")
        competition = Competition.objects.get(name="competition")
        breed = Breed.objects.get(name="malamute")
        dog = Dog.objects.get(name="doggo")
        award = Award.objects.get(name="thebest")
        participation = Participation.objects.get(name="participation")

        print("Testing Sport and Competition...")
        self.assertEqual(competition.sport, sport, "Sport and Competition relation dont match.")
        print("Testing Breed and Dog...")
        self.assertEqual(dog.breed, breed, "Dog and Breed relation dont match.")
        print("Testing Competition and Participation...")
        self.assertEqual(participation.competition, competition, "Participation and Competition relation dont match.")
        print("Testing Dog and Participation...")
        self.assertEqual(participation.dog, dog, "Participation and Dog relation dont match.")
        print("Testing Competition and Dog...")
        self.assertEqual(Participation.objects.get(dog=dog), Participation.objects.get(competition=competition), "Competition and Dog relation dont match.")
        print("Testing Participation and Award...")
        self.assertEqual(award, participation.award, "Award and Participation relation dont match.")
        print("All passed.")


    def test_ViewResponse(self): 

        print("\nT3: Testing view function responses - testing on 0,1,2 text slug input views - ")
        
        # Retrieve objects again (fine from first test)
        sport = Sport.objects.get(name="football")
        competition = Competition.objects.get(name="competition")
        breed = Breed.objects.get(name="malamute")
        dog = Dog.objects.get(name="doggo")
        award = Award.objects.get(name="thebest")
        participation = Participation.objects.get(name="participation")

        print("Testing sport homepage view (no slug input requirement):")
        # get response and context (context for this should be a queryset of sport)
        response = self.client.get(reverse('rango:sports')) # kwargs={'breed_name_slug': breed.slug, 'dog_slug': dog.slug}))
        context = response.context
        self.assertEqual(context['sports'].first(), sport, "Context of Sport from sport homepage response does not match")

        print("Testing sport profile view (one slug input requirement): ")
        response = self.client.get(reverse('rango:sports_name', kwargs={'sports_name_slug': sport.slug})) # kwargs={'breed_name_slug': breed.slug, 'dog_slug': dog.slug}))
        context = response.context
        self.assertEqual(context['sport'], sport, "Context of Sport from sport profile does not match.")
        self.assertEqual(context['competitions'].first(), competition,"Context of Competition from sport profile does not match." )
    
        print("Testing dog profile view (two slug input requirement): ")
        response = self.client.get(reverse('rango:dog_profile', kwargs={'breed_name_slug': breed.slug, 'dog_slug': dog.slug})) # kwargs={'breed_name_slug': breed.slug, 'dog_slug': dog.slug}))
        context = response.context
        self.assertEqual(context['dog'], dog, "Context of Dog from dog profile does not match.")
        self.assertEqual(context['breed'], breed,"Context of Breed from dog profile does not match." )
        self.assertEqual(context['participations'].first(), participation,"Context of Participation from dog profile does not match." )
       
        print("All passed.")


    def test_UserLogin(self):
        
        print ("\nT4: Testing user login -")
        c = Client()
        response = c.post('/accounts/login/', {'username': 'bob', 'password': 'workplease123'})
        context = response.context
        self.assertEquals(response.status_code, 302,"Error in login attempt.")
        print("All passed.")









        