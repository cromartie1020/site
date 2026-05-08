from django.shortcuts import render
from bs4 import BeautifulSoup
import requests



# Create your views here.
def home(request):
    return render(request, 'base.html')


def profile(request):
    return render(request, 'profile.html')

def news(request):
    url = 'https://www.pythonanywhere.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    context = {
        'uername':haynes,
        'password':Hayneslorena2912#
    }    
    
    return render(request, 'core/pythonanywhere.html')
