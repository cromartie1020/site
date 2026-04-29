from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def profile(request):
    return render(request, 'profile.html')