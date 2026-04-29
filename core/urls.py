from django.urls import path,include
from . import views
urlpatterns = [
    # Define your URL patterns here
    path('', views.home, name='home'),
    
]
