from django.urls import include, path
from rest_framework import routers
from . import views
from .views import *

router = routers.DefaultRouter()
router.register(r'notesheet', views.NoteSheetViewSet)
router.register(r'faculty', views.FacultyDetailsViewSet)
router.register(r'allUsers', views.AllFacultyUsersViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('current_user/', get_current_user),
    path('users/create', CreateUserView.as_view())
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
