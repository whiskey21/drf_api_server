from rest_framework import serializers
from .models import Member, Enterance
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'id',
            'name',
            'phoneNum',
        )

class EnteranceSerializer(serializers.ModelSerializer):
    info = MemberSerializer(read_only=True)
    class Meta:
        model = Enterance
        fields = (
            'eid',
            'memberID',
            'info',
            'enterance_time',
        )
        read_only_fields = ('enterance_time',)
