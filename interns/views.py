from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import InterestForm, RegisteredUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_protect

def aboutus(request):
    return render(request, 'aboutus.html')

def bootstrapinternship(request):
    return render(request, 'bootstrapinternship.html')

def contact(request):
    return render(request, 'contact.html')

def cssinternship(request):
    return render(request, 'cssinternship.html')

def mybookmark(request):
    return render(request, 'mybookmark.html')

def dashboard_my_profile(request):
    return render(request, 'dashboard-my-profile.html')

def development(request):
    return render(request, 'development.html')

def djangointernship(request):
    return render(request, 'djangointernship.html')

def faq(request):
    return render(request, 'faq.html')

def fullstackwithpython(request):
    return render(request, 'fullstackwithpython.html')

def hrinternship(request):
    return render(request, 'hrinternship.html')

def htmlinternship(request):
    return render(request, 'htmlinternship.html')

def index(request):
    return render(request, 'index.html')

def internships(request):
    return render(request, 'internships.html')

def javainternship(request):
    return render(request, 'javainternship.html')

def javascriptinternship(request):
    return render(request, 'javascriptinternship.html')

def jqueryinternship(request):
    return render(request, 'jqueryinternship.html')

def pages_404(request):
    return render(request, 'pages-404.html')

def pages_blog(request):
    return render(request, 'pages-blog.html')

def pages_masonry_filtering(request):
    return render(request, 'pages-masonry-filtering.html')

def programming(request):
    return render(request, 'programming.html')

def pythoninternship(request):
    return render(request, 'pythoninternship.html')

def user_profile(request):
    return render(request, 'user-profile.html')

def webdesigning(request):
    return render(request, 'webdesigning.html')
def coming_soon(request):
    return render(request, 'comingsoon.html')







