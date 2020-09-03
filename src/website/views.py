from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectsSerializer, MembersSerializer, ContactSerializer
from .models import Projects, Members, Contact
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
