from rest_framework import serializers
from .models import Projects, Members, Contact, Event, Registration

class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Projects
        fields='__all__'


class MembersSerializer(serializers.ModelSerializer):

    class Meta:
        model=Members
        fields='__all__'


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model=Contact
        fields='__all__'


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model=Event
        fields='__all__'


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Registration
        fields='__all__'

