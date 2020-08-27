from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework import status

from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models

from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions


class HelloApiView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return a list of api features"""
        an_apiview = [
            'Uses HTTP method as functions (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over you api logiv',
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """recieve our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    '''function for viewsets'''

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''return a hello message'''

        a_viewset = [
            '1st string',
            '2nd string',
            'third string',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        '''create a new hello msg'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            messgae = f"hello {name}"
            return Response({'messgae': messgae})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request, pk=None):
        '''handle getting an object by its id'''
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        '''handle updating objects'''
        return Response({'http_method': 'PUT'})

    def delete(self, request, pk=None):
        '''handle deleting objects'''
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    '''handle creating and updating profiles'''
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
