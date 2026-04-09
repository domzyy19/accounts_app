'''to create a route/url : we need the path import'''
from django.urls import path 
'''django auths view : to give access to configured
authenication operations in django'''
'''import the custom views functionalities'''
from . import views
## give a label for the routes : 'accounts:login'
app_name = 'media_assets'
## register the urls paths by mapping to appropriate
## view method 
urlpatterns = [
    # '' : root path : 8000/
    path('', views.dashboard_view, 
    name='dashboard'),
    
    
]