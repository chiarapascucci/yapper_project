from django.test import TestCase
from rango.models import Sport, Dog, Competition, Breed, Award, Participation
import random as rand
import datetime
import os
import inspect

# Create your tests here.

class ModelUnitTests(TestCase):

    def test_setup(self):
        
        print("Setting up Unit test for Models...\n")

        # Instantiate differnt entites and populate  

        # Sport entity 
        sport = Sport.objects.create(name="football")
        sport.description = 'description'
        sport.breed_restrictions = 'none'
        sport.follows = 10

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



    def test_ModelRelationAndValueTests(self):

        print("Testing model relations and values:\n\n")
        
        # Fetch entities
        print("T1: Testing object retrieval from SQLite DB: ")

        sport = Sport.objects.filter(name="football")
        competition = Competition.objects.filter(name="competition")
        breed = Breed.objects.filter(name="malamute")
        dog = Dog.objects.filter(name="doggo")
        award = Award.objects.filter(name="thebest")
        participation = Participation.objects.filter(name="participation")

        self.assertIsNotNone(sport,         'Sport does not exist.')
        self.assertIsNotNone(competition,   'Competition does not exist.')
        self.assertIsNotNone(breed,         'Breed does not exist.')
        self.assertIsNotNone(dog,           'Dog does not exist.')
        self.assertIsNotNone(award,         'Award does not exist.')
        self.assertIsNotNone(participation, 'Participation does not exist.')

            




    





        