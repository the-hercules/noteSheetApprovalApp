from rest_framework import serializers

from .models import NoteSheet, FacultyDetails


class NoteSheetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NoteSheet
        fields = ('url', 'id', 'f_id', 'date', 'school', 'department', 'subject', 'description', 'objective'
                  , 'proposal_details', 'proposal_submitted_by', 'proposal_submitted_by_1'
                  , 'receiver_1', 'receiver_2', 'Status')


class FacultyDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FacultyDetails
        fields = ('employee_id', 'Name')
