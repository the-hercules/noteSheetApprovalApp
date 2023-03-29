from rest_framework import serializers

from .models import NoteSheet, FacultyDetails, AllFacultyUsers
from django.contrib.auth.models import User
from rest_framework.settings import api_settings


class NoteSheetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NoteSheet
        # fields = ('url', 'id', 'f_id', 'date', 'school', 'department', 'subject', 'description', 'objective'
        #           , 'proposal_details', 'proposal_submitted_by', 'proposal_submitted_by_1'
        #           , 'receiver_1', 'receiver_2', 'Status')
        fields = ('__all__')


class FacultyDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FacultyDetails
        fields = ('employee_id', 'Name')


class AllFacultyUsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllFacultyUsers
        # fields=('username','password','employee_id','first_name','last_name','designation',
        #         'school', 'mobile_number','email_address')
        fields = ('__all__')


# adding searizers for auth

class GetFullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_superuser', 'first_name', 'last_name')


class UserSerializerWithToken(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    def get_token(self, object):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)

        return token

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name',
                  'last_name')
