from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile, Competition, Sport

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

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)


class CompetitionForm(forms.ModelForm):
    name = forms.CharField(max_length=Competition.NAME_MAX_LENGTH,
                           help_text="Please enter the name of the competition:" )
    address = forms.CharField(max_length=Competition.ADDRESS_MAX_LENGTH,
                                help_text="Please enter the address:")
    location = forms.CharField(max_length=100,
                                help_text="Please enter the coordinates...:")
    date = forms.DateTimeField(help_text="Please enter the date it will commence:")
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