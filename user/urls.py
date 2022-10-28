"""All_In_One URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView

from user import views
from All_In_One import settings
from django.conf.urls.static import static

urlpatterns = [
    #
    # path('', TemplateView.as_view(template_name='home/index.html'), name='home'),

    path('', views.home, name='home'),
    path('get_it_yours/', views.get_it_yours, name='get_it_yours'),
    path('about-us/', views.about_us, name='about-us'),

    path('signup/', views.signup, name='signup'),
    path('email-verify', views.VerifyEmail.as_view(), name="email-verify"),
    path('logout/', views.logoutt, name='logout'),
    path('login_signup/', views.login_signup, name='login_signup'),
    path('cloths/', views.cloths, name='cloths'),
    path('food/', views.food, name='food'),
    # path('hero/',views.hero,name='hero'),
    path('music/', views.Music.as_view(), name='music'),
    path('Filims/', views.filims, name='Filims'),
    path('Wines/', views.wines, name='Wines'),
    path('Transport/', views.transport, name='Transport'),
    path('Tourism/', views.tourism, name='Tourism'),
    path('Books/', views.books, name='Books'),
    path('Electronics/', views.electronics, name='Electronics'),
    path('Interiors/', views.interiors, name='Interiors'),
    path('heros/',views.hero,name='hero'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('change_password/<token>',views.change_password,name='change_password'),
    path('editemployee/<str:pk>',views.editemployee,name='editemployee')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
