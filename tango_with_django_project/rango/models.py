from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


"""
Yapper models 
"""

class Breed(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Breed, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Breeds"


    def __str__(self):
        return self.name


class Dog(models.Model):
    
    # Necessary
    dog_id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length=128)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    #owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)        # Temp blank until Users properly implemented

    # Add follows

    # Optionally filled
    main_about = models.TextField(blank=True, default="")    # Dog's editable description, allow blank
    # Temp location before dynamic file path
    display_pic = models.ImageField(upload_to="dog_profiles/temp", blank=True) # Specify dimension max/resize later

    #sports = models.ManyToManyField(Sport, on_delete=models.CASCADE)
    #competitions = models.ManyToManyField(Competition, on_delete=models.CASCADE)

    # Name slug for use in URLs
    slug = models.SlugField(unique=True)

    # Table stat info
    SEX_CHOICES = (("Female","Bitch"), ("Male","Dog"), ("Unknown","Unknown"), (None, " "))
    sex = models.CharField(max_length = 10, choices=SEX_CHOICES, blank=True)
    #dob = models.DateField(default = None, blank=True)

 
    def save(self, *args, **kwargs):
        # Update slug
        self.slug = slugify("{self.dog_id}-{self.name}".format(self=self))
        print(str(self.slug))

        # Set media path dynamically if still set to default --- probably wrong now, just do this when a form is sent
#        if self.display_pic.storage.location == "dog_profiles/temp":
#            self.display_pic.storage.location = "dog_profiles/{}-{}".format(self.dog_id,self.slug)
#            print(self.display_pic.storage.location)

        # Finish up with normal save function
        super(Dog, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Dogs"

    def __str__(self):
        return str(self.dog_id) + " " + self.name + ", " + self.breed.name

    # Full debug method, prints all attributes of dog instance
    def printDog(self):
        for a in dir(self):
            if not a.startswith("__") and not callable(getattr(self,a)):
                print(a)



class Sport(models.Model):
    
    # Enforce consistent name length accross all instances
    NAME_MAX_LENGTH = 128

    # Model attributes 
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    description = models.TextField()
    breed_restricitons = models.TextField()

    # Slug attributes
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sport, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class Competition(models.Model):
    
    # Enforce consistent name length accross all instance
    NAME_MAX_LENGTH = 128
    ADDRESS_MAX_LENGTH = 200
    URL_MAX_LENGTH = 200

    # Model attributes 
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    address = models.CharField(max_length=ADDRESS_MAX_LENGTH)   # Address of compititon
    location = models.CharField(max_length=100)                 # Google API information in String form
    date = models.DateField(null = True)                        # Date object
    eventpage = models.URLField()                               # Url of event page if avaialble
    isCompleted = models.BooleanField(default=False)            # Boolean field for is completed or not 
    description = models.TextField()                            # Description about competition

    # Relationship attribute 
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    # Slug attributes
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Competition, self).save(*args, **kwargs)

    # Verbose print
    def __str__(self):
        return self.name



class Participation(models.Model):
    pass

class Award(models.Model):
    pass




