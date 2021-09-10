from rest_framework import serializers
from .models import Member
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Member
        fields = (
            'user',
            'id',
            'name',
            'email',
            'info',
            'created_at',
        )
        read_only_fields = ('created_at',)