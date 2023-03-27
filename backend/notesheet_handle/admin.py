from django.contrib import admin
from .models import NoteSheet, FacultyDetails, AllFacultyUsers

# Register your models here.

admin.site.register(NoteSheet)
admin.site.register(FacultyDetails)
admin.site.register(AllFacultyUsers)
