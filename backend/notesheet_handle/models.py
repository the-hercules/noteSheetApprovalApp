from django.db import models


# Create your models here

# class AllFacultyUsers(models.Model):
#     username = models.CharField()
#     password = models.CharField(max_length=25)
#     employee_id = models.CharField(max_length=20)
#     name = models.CharField()
#     Dob = models.DateField()
#

# class SenderDetails(models.Model):
#     sender_id = models.ForeignKey(AllFacultyUsers, on_delete=models.SET_NULL)
#     sender = models.CharField(max_length=50)

class FacultyDetails(models.Model):
    employee_id = models.CharField(max_length=20)
    Name = models.CharField(max_length=50)


# this sender field is tentative

class NoteSheet(models.Model):
    f_id = models.ForeignKey(
        FacultyDetails, on_delete=models.SET_NULL,null=True)
    date = models.DateTimeField(auto_now_add=True)
    # date = models.DateTimeField(format='%d-%m-%Y %H:%M', auto_now_add=True)
    subject = models.TextField()
    school = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    description = models.TextField()
    objective = models.TextField()
    proposal_details = models.TextField()
    proposal_submitted_by = models.CharField(max_length=255)
    proposal_submitted_by_1 = models.CharField(max_length=255)
    receiver_1 = models.CharField(max_length=255)
    receiver_2 = models.CharField(max_length=255)
    Status = models.IntegerField(default='000')

# class NoteSheetAdditional(models.Model):
#     f_id = models.ForeignKey(NoteSheet, on_delete=models.SET_NULL, null=True)
#     Status = models.IntegerField()
