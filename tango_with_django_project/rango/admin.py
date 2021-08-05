from django.contrib import admin
from rango.models import Category, Page, UserProfile, Sport, Competition, Dog, Breed, Participation, Award
from rango.models import UserProfile
from rango.models import Sport

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class SportAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CompetitionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}




admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(Sport, SportAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Dog)
admin.site.register(Breed)

admin.site.register(Participation)
admin.site.register(Award)
