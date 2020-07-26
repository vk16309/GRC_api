from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from student import serializers
from student import models
from student import permissions
#------------------------------------------------------------------------------------------------------#

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle Creating and upadting profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserComplaintViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating complaint items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ComplaintSerializer
    queryset = models.Complaint.objects.all()
    permission_classes = (permissions.UpdateOwnComplaint,IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category','sub_category','complaint_text')

    def perform_create(self,serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user, institute_name=self.request.user.institute)
