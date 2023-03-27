from rest_framework import serializers

from .models import NoteSheet, FacultyDetails, AllFacultyUsers


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
