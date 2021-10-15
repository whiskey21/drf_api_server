from django.shortcuts import render

from rest_framework import viewsets
from .serializers import MemberSerializer
from .models import Member
from rest_framework import permissions

class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
