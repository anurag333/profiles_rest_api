from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework import status

from profiles_api import serializers


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
