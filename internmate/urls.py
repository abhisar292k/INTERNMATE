"""
URL configuration for internamte project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from interns import views

urlpatterns = [
    path('aboutus/', views.aboutus, name='aboutus'),
    path('bootstrapinternship/', views.bootstrapinternship, name='bootstrapinternship'),
    path('contact/', views.contact, name='contact'),
    path('cssinternship/', views.cssinternship, name='cssinternship'),
    path('mybookmark/', views.mybookmark, name='mybookmark'),
    path('dashboard-my-profile/', views.dashboard_my_profile, name='dashboard_my_profile'),
    path('development/', views.development, name='development'),
    path('djangointernship/', views.djangointernship, name='djangointernship'),
    path('faq/', views.faq, name='faq'),
    path('fullstackwithpython/', views.fullstackwithpython, name='fullstackwithpython'),
    path('hrinternship/', views.hrinternship, name='hrinternship'),
    path('htmlinternship/', views.htmlinternship, name='htmlinternship'),
    path('', views.index, name='index'),
    path('internships/', views.internships, name='internships'),
    path('javainternship/', views.javainternship, name='javainternship'),
    path('javascriptinternship/', views.javascriptinternship, name='javascriptinternship'),
    path('jqueryinternship/', views.jqueryinternship, name='jqueryinternship'),
    path('pages-404/', views.pages_404, name='pages_404'),
    path('pages-blog/', views.pages_blog, name='pages_blog'),
    path('pages-masonry-filtering/', views.pages_masonry_filtering, name='pages_masonry_filtering'),
    path('programming/', views.programming, name='programming'),
    path('pythoninternship/', views.pythoninternship, name='pythoninternship'),
    path('user-profile/', views.user_profile, name='user_profile'),
    path('webdesigning/', views.webdesigning, name='webdesigning'),
    path('comingsoon/', views.coming_soon, name='coming_soon'),
]
