import json
from itertools import chain

from django.core.serializers import serialize
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db.models import Q
from .models import NoteSheet, FacultyDetails, AllFacultyUsers
from .serializers import NoteSheetSerializer, FacultyDetailsSerializer, AllFacultyUsersSerializer, UserSerializer

from .searializers import *


# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import permissions
#

# class NoteSheetViewSet(viewsets.ModelViewSet):
#     # class NoteSheetViewSet(generics.ListCreateAPIView):
#     queryset = NoteSheet.objects.all()
#     serializer_class = NoteSheetSerializer



class NoteSheetViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSheetSerializer
    #for jwt
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return NoteSheet.objects.all()
        else:
            return NoteSheet.objects.filter(Q(proposal_submitted_by=user.username) | Q(receiver_1=user.username) | Q(receiver_2=user.username)).distinct()

class FacultyDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = FacultyDetailsSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return FacultyDetails.objects.all()
        else:
            return FacultyDetails.objects.filter(employee_id=user.username)


class AllFacultyUsersViewSet(viewsets.ModelViewSet):
    serializer_class = AllFacultyUsersSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return AllFacultyUsers.objects.all()
        else:
            return AllFacultyUsers.objects.filter(username=user.username)

#
# class FacultyDetailViewSetBYID(viewsets.ModelViewSet):
# queryset = FacultyProfile.objects.filter(user=)



@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def get_current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)














# for auth
@api_view(['GET'])
def get_current_user(request):
    # print(request.token)
    serializer = GetFullUserSerializer(request.user)
    # print(request.user.id)

    return Response(serializer.data)


@api_view(['GET'])
def get_faculty_profile(request):
    r_id = request.user.id
    data = FacultyProfile.objects.filter(user=r_id).values('is_admin', 'employee_id', 'designation', 'school',
                                                           'department', 'mobile_number', 'email_address')
    data2 = User.objects.filter(id=r_id).values('first_name', 'last_name')
    qset = list(chain(data, data2))
    fset = {}
    for i in qset:
        for key, value in i.items():
            fset[key] = value
    return HttpResponse(json.dumps(fset), content_type='application/json')


# @api_view(['POST'])
# def get_user(request):


class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        user = request.data.get('user')
        if not user:
            return Response({'response': 'error', 'message': 'No data found'})
        serializer = UserSerializerWithToken(data=user)
        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            return Response({"response": "error", "message": serializer.errors})
        return Response({"response": "success", "message": "user created successfully"})
