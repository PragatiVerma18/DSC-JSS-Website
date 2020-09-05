from django.urls import path, include
from .views import *
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register('projects',ProjectViewSet)
routers.register('members',MemberViewSet)
routers.register('contact',ContactViewSet)
routers.register('event',EventViewSet)
routers.register('register',RegistrationViewSet)



urlpatterns = [
   path('',include(routers.urls)),
]
