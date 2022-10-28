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

from All_In_One import settings
from django.conf.urls.static import static

from dashboard import views

urlpatterns = [
    #
    # path('', TemplateView.as_view(template_name='home/index.html'), name='home'),
    path('dashboard_types/',views.dashboard_types,name='dashboard_types'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('view_dashboard/<str:pk>',views.view_dashboard,name='view_dashboard'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('persional_profile/',views.persional_profile,name='persional_profile'),
    path('review_ratings/',views.review_ratings,name='review_ratings'),
    path('review/',views.rate,name='review'),
    path('submit_review/',views.submit_review,name='submit_review'),
    path('display_feedback/',views.display_feedback,name='display_feedback'),
    path('super_login/',views.super_login,name='super_login'),
    path('index2/',views.index2,name='index2'),
      path('index3/',views.index3,name='index3'),
      path('event_management/',views.event_management,name='event_management'),
      path('all_professors/',views.all_professors,name='all_professors'),
      path('add-professor/',views.add_professor,name='add-professor'),
      path('edit-professor/',views.edit_professor,name='edit-professor'),
      path('professor-profile/',views.professor_profile,name='professor-profile')


   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
