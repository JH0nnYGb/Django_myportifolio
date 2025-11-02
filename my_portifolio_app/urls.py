from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home_my_profile_django'),
    path('projects/', views.project, name='my_projects'),
    path('my_activities/', views.activities, name='my_activities'),
    path('my_graduations/', views.graduations, name='my_graduations'),
]
