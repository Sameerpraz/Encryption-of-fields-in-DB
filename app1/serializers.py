from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers
from cryptography.fernet import Fernet


# token = f.encrypt(b"A really secret message. Not for prying eyes.")
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    

    def create(self, validated_data):
        customer = Customer.objects.create(**validated_data)
        return customer