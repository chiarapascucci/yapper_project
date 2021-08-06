from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from django_google_maps import fields as map_fields
import tango_with_django_project.settings as settings
from django.core.files.storage import FileSystemStorage

# Storage systsem for certificates
#certificate_storage = FileSystemStorage(location='/media/dogcertificates/')


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




# GMaps stuff
class GMap(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

    def __str__(self):
        return self.address



class Breed(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    follows = models.PositiveIntegerField(default=0)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Breed, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Breeds"


    def __str__(self):
        return self.name

class Sport(models.Model):
    
    # Enforce consistent name length accross all instances
    NAME_MAX_LENGTH = 128

    # Model attributes 
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    description = models.TextField()
    breed_restrictions = models.TextField()
    follows = models.IntegerField(default=0)
    image = models.ImageField(blank=True)

    # Slug attributes
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sport, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

        
class Dog(models.Model):

    # Necessary
    #dog_id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length=128)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    #owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)        # Temp blank until Users properly implemented

    follows = models.PositiveIntegerField(default=0)

    # Optionally filled
    main_about = models.TextField(blank=True, default="")    # Dog's editable description, allow blank
    # Temp location before dynamic file path
    display_pic = models.ImageField(upload_to="dog_profiles/temp", width_field=550, height_field=550, blank=True) # Specify dimension max/resize later

    #competitions = models.ManyToManyField(Competition, on_delete=models.CASCADE)

    # Name slug for use in URLs
    slug = models.SlugField(unique=True)

    # Table stat info
    SEX_CHOICES = (("Female","Bitch"), ("Male","Dog"), ("Unknown","Unknown"), (None, " "))
    sex = models.CharField(max_length = 10, choices=SEX_CHOICES, blank=True)
    #dob = models.DateField(default = None, blank=True)

 
    def save(self, *args, **kwargs):
        # setup slug to reflect none id before save (when dog-id autofield fills)
        #if self.id is None:
        #self.slug = slugify("{self.name}".format(self=self))
        self.slug = slugify("{self.id}-{self.name}".format(self=self))
        super(Dog, self).save(*args, **kwargs)

        # Set media path dynamically if still set to default --- probably wrong now, just do this when a form is sent
#        if self.display_pic.storage.location == "dog_profiles/temp":
#            self.display_pic.storage.location = "dog_profiles/{}-{}".format(self.id,self.slug)
#            print(self.display_pic.storage.location)

    class Meta:
        verbose_name_plural = "Dogs"

    def __str__(self):
        return str(self.id) + " " + self.name + ", " + self.breed.name



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    followed_breeds = models.ManyToManyField(Breed, blank=True)
    followed_sports = models.ManyToManyField(Sport, blank=True)
    followed_dogs= models.ManyToManyField(Dog, blank=True)
    bio = models.CharField(max_length=300, blank=True)

    latitude = models.DecimalField(max_digits=9,decimal_places=6, blank=True, default=0)
    longitude = models.DecimalField(max_digits=9,decimal_places=6, blank=True, default=0)
    loc_image = models.URLField(blank=True)

    picture = models.ImageField(upload_to='profile_images', default='profile_images/default.jpg', blank=True)
    user_slug = models.SlugField(unique=True)
    owned_dogs = models.ManyToManyField(Dog, blank=True, related_name='dogs')
    
    is_owner = models.BooleanField(default=False)
    is_comp_org = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        self.user_slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def set_Follows(self, field):
        self.follows = field

    def __str__(self):
        return self.user.username



class Competition(models.Model):
    
    # Enforce consistent name length accross all instance
    NAME_MAX_LENGTH = 128
    ADDRESS_MAX_LENGTH = 200
    URL_MAX_LENGTH = 200

    # Model attributes 
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    address = models.CharField(max_length=ADDRESS_MAX_LENGTH)   # Address of compititon
    location = models.CharField(max_length=100, null=True)      # Google API information in String form
    date = models.DateField(null=True)                          # Date object
    eventpage = models.URLField(null=True)                      # Url of event page if avaialble
    isCompleted = models.BooleanField(default=False)            # Boolean field for is completed or not 
    description = models.TextField(null=True)                   # Description about competition
    image = models.ImageField(blank=True)

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


# User should not need to interact with these models as they are used to hold information
# on the relation between dog and competitions (N:M -> 1:N and 1:M)

class Award(models.Model):

    # Enforce consistent name length accross all instance
    NAME_MAX_LENGTH = 128

    # Model attributes 
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    description = models.TextField()                            # Description about award
    certificate = models.FileField(upload_to= 'media/dogcertificates/')                            #storage=certificate_storage
    certificate_path = models.CharField(max_length=500)

    # Verbose print
    def __str__(self):
        return self.name


class Participation(models.Model):
    
    # Enforce consistent name length accross all instance
    NAME_MAX_LENGTH = 128

    # Model for entity relation breakdown between dogs and competition
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)

    # Allow null to be true as award only awarded if competition complete
    award = models.OneToOneField(Award, null=True, on_delete=models.CASCADE)
    
    # Verbose print
    def __str__(self):
        return self.name





