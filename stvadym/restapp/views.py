from django.contrib.auth.models import User
from stvadym.restapp.models import Note
from rest_framework import viewsets
from stvadym.restapp.serializers import UserSerializer, NoteSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(username=self.request.user)
        return query_set


class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(userId=self.request.user)
        return query_set
