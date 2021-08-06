from django.test import TestCase
from rango.models import Sport, Dog, Competition, Breed, Award, Participation
import random as rand
import datetime
import os
import inspect

# Create your tests here.

class ModelUnitTests(TestCase):

    def setUp(self):
        

        # Instantiate differnt entites and populate  
        # Sport entity 
        sport = Sport.objects.create(name="football")

        # Competition entity
        competition = Competition.objects.create(name="competition",sport=sport)
        competition.address = "address"
        competition.date = datetime.date(2021,10,22)
        competition.eventpage = "http:/www.youtube.com"

        # Breed emtity
        breed = Breed.objects.create(name="malamute")
        breed.description = "description"
        breed.follows = 20

        # Dog entity
        dog = Dog.objects.create(name="doggo", breed=breed)
        dog.main_about = "description"
        dog.follows = 30

        # Award entity
        award = Award.objects.create(name="thebest")
        award.description = "description"
        certificate_path = "pathtofglory"

        # Participation entity
        participation = Participation.objects.create(name = "participation", dog=dog, competition=competition, award=award)



    def test_ModelAttributeRetrieval(self):

        print("Testing model relations and values:\n\n")
        
        # Fetch entities
        print("T1: Testing object retrieval from SQLite DB - ")
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


    def test_ModelRelations(self):

        print("T2: Testing model relationships - ")
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






    





        