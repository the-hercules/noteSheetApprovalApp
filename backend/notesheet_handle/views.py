# from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework import generics
# Create your views here.
from .models import NoteSheet, FacultyDetails, AllFacultyUsers
# from .searializers import NoteSheetSerializer, FacultyDetailsSerializer, AllFacultyUsersSerializer
from .searializers import *


# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import permissions
#

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

# for auth
# @api_view(['GET'])
# def get_current_user(request):
#     serializer = GetFullUserSerializer(request.user)
#     return Response(serializer.data)
#

# class CreateUserView(APIView):
#     permission_classes = (permissions.AllowAny,)
#
#     def post(self, request):
#         user = request.data.get('user')
#         if not user:
#             return Response({'response': 'error', 'message': 'No data found'})
#         serializer = UserSerializerWithToken(data=user)
#         if serializer.is_valid():
#             saved_user = serializer.save()
#         else:
#             return Response({"response": "error", "message": serializer.errors})
#         return Response({"response": "success", "message": "user created successfully"})
