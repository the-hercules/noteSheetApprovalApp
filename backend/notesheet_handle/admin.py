from django.contrib import admin
from .models import NoteSheet, FacultyDetails, FacultyProfile

# Register your models here.

admin.site.register(NoteSheet)
admin.site.register(FacultyDetails)
admin.site.register(FacultyProfile)
