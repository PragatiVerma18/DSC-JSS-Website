from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectsSerializer, MembersSerializer, ContactSerializer, EventSerializer, RegistrationSerializer
from .models import Projects, Members, Contact, Event, Registration
# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Projects.objects.all()
    serializer_class=ProjectsSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset=Members.objects.all()
    serializer_class=MembersSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset=Registration.objects.all()
    serializer_class=RegistrationSerializer
