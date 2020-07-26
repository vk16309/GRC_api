from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method is permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnComplaint(permissions.BasePermission):
    """Allow user to update their own complaint"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to upadte their own status"""
        if request.method is permissions.SAFE_METHODS:
            return True
        if request.user.is_redressal:
            obj.status=True
            return True 
        return obj.user_profile.id == request.user.id
