from django.shortcuts import render

def home(request):
    return render(request, 'home.html')         # take us to home page