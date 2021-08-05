from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile, Breed, Dog, Competition, Sport, GMap
from django_google_maps.widgets import GoogleMapsAddressWidget

from django.forms.fields import CharField
from django.forms.widgets import HiddenInput
import datetime as dt

# We could add these forms to views.py, but it makes sense to split them off into their own file.

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.NAME_MAX_LENGTH, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)
    
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        
        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password', )

class UserProfileForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    bio = forms.CharField(max_length=300)
    location = forms.CharField(max_length=128)
    picture = forms.ImageField()
    class Meta:
        model = UserProfile
        fields = ('bio', 'picture', 'location',)


"""
    Yapper forms
"""

# Add owner here
class AddDogForm(forms.ModelForm):
    name = forms.CharField(max_length=128, required=True, help_text="Enter dog name")
    breed = forms.ModelChoiceField(queryset=Breed.objects.all(), empty_label="Select", help_text="Select a breed", required=True)
    #owner = forms.HiddenInput()
    main_about = forms.CharField(max_length=1000, help_text="Tell us about your canine!")
    follows = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

#    sex = forms.ChoiceField()

    class Meta:
        model = Dog
        # Add owner to args
        fields = ('name', 'breed', 'main_about',)


class EditDogForm(forms.ModelForm):
    """
    Stuff to allow to edit:
    main_about, display_pic, file_upload, achievements
    """


class CompetitionForm(forms.ModelForm):
    name = forms.CharField(max_length=Competition.NAME_MAX_LENGTH,
                           help_text="Please enter the name of the competition:" )
    address = forms.CharField(max_length=Competition.ADDRESS_MAX_LENGTH,
                                help_text="Please enter the address:")
    location = forms.CharField(max_length=100,
                                help_text="Please enter the coordinates...:")
    date = forms.DateField(help_text="Please enter the date it will commence:")
    eventpage = forms.URLField(help_text="Please enter the url of the competition/event page:")
    isCompleted = forms.BooleanField(help_text="Is the competition already complete and this is just for storing?")
    description = forms.Textarea()

    # Get sport 
    sport = forms.ModelChoiceField(queryset=Sport.objects.all(), help_text="Select a sport of the competition:")

    class Meta:
        model = Competition
        fields = ('name', 'address', 'location', 'date', 'eventpage', 'description', 'sport')
    
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
            
