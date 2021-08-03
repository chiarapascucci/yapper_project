
from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name = 'index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('restricted/', views.restricted, name='restricted'),
 
    path('sports/', views.sports_homepage, name='sports'),                          # =========== Start of yapper urls
    path('sports/<slug:sports_name_slug>/', views.sports_profile, name='sports_name'),        
    path('breeds/', views.breed_homepage ,name='breeds'),
    path('breeds/breed_name/', views.breed_profile ,name='breed_name'),             # Requires dynamic slug field
    path('breeds/breed_name/dog_name/', views.dog_profile ,name='dog_name'),        # Requires dynamic slug field
    path('competitions/', views.competition_homepage, name='competitions'), 
    path('competitions/<slug:competition_name_slug>/', views.competition_profile ,name='competition_name'),    
    path('help/', views.faq ,name='help'),  # Should this not be url faq/ ?
    path('user/', views.user_profile ,name='user'),                                                 # Requires dynamic slug field
    path('user/add_dog/', views.add_dog, name='add_dog'),
    path('user/edit/', views.user_profile_edit ,name='edit'),
    path('user/register_competition/', views.add_competition, name='register_competition'),
]
