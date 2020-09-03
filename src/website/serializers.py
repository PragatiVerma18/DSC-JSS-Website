from rest_framework import serializers
from .models import Projects, Members, Contact

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