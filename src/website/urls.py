from django.urls import path, include
from .views import *
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register('projects',ProjectViewSet)
routers.register('members',MemberViewSet)
routers.register('contact',ContactViewSet)


urlpatterns = [
   path('',include(routers.urls)),
]
