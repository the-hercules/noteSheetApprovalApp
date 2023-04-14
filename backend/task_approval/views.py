from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer


# class FacultyProfileView(viewsets.ModelViewSet):
    # queryset = FacultyProfile.objects.filter(id=)
    # serializer_class = FacultyProfileSerializer
