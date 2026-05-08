from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

session = requests.Session()

# Create your views here.
def home(request):
    return render(request, 'base.html')


def profile(request):
    return render(request, 'profile.html')

def pythonanywhere(request):
    url = 'https://www.pythonanywhere.com'
    response = requests.get(url)
   
    context = {
        'username':'haynes',
        'password':'Hayneslorena2912#'
    }    
    session.post(url, data=context)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    return render(request, 'core/pythonanywhere.html')
