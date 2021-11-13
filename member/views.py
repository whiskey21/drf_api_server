from datetime import datetime

from django.shortcuts import render

from rest_framework import viewsets
from .serializers import MemberSerializer, EnteranceSerializer
from .models import Member, Enterance
from rest_framework import permissions

class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EnteranceView(viewsets.ModelViewSet):
    queryset = Enterance.objects.all()
    serializer_class = EnteranceSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()

class EnteranceDateView(viewsets.ModelViewSet):
    queryset = Enterance.objects.filter(enterance_time=datetime(2021, 10, 15))
    serializer_class = EnteranceSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()
