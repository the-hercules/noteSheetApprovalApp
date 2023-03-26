# from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework import generics
# Create your views here.
from .models import NoteSheet, FacultyDetails, AllFacultyUsers
from .searializers import NoteSheetSerializer, FacultyDetailsSerializer, AllFacultyUsersSerializer


class NoteSheetViewSet(viewsets.ModelViewSet):
    # class NoteSheetViewSet(generics.ListCreateAPIView):
    queryset = NoteSheet.objects.all()
    serializer_class = NoteSheetSerializer


#
class FacultyDetailsViewSet(viewsets.ModelViewSet):
    # class NoteSheetViewSet(generics.ListCreateAPIView):
    queryset = FacultyDetails.objects.all()
    serializer_class = FacultyDetailsSerializer


class AllFacultyUsersViewSet(viewsets.ModelViewSet):
    queryset = AllFacultyUsers.objects.all()
    serializer_class = AllFacultyUsersSerializer
