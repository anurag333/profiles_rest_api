from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''allow users to update their profile'''

    def has_object_permission(self, request, view, obj):
        '''check if user is trying to update own profile'''

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    '''allow users to update their status '''

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
