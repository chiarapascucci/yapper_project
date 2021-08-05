from django.contrib import admin
from rango.models import Category, Page, UserProfile, Sport, Competition, Dog, Breed, Participation, Award
from rango.models import UserProfile
from rango.models import Sport

from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class SportAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CompetitionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class DogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class BreedAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# GMaps
class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }




admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(Sport, SportAdmin)
admin.site.register(Competition, CompetitionAdmin)
<<<<<<< HEAD
admin.site.register(Dog, DogAdmin)
admin.site.register(Breed, BreedAdmin)
=======
admin.site.register(Dog)
admin.site.register(Breed)

admin.site.register(Participation)
admin.site.register(Award)
>>>>>>> main
