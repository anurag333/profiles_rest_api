from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        """return a list of api features"""
        an_apiview = [
            'Uses HTTP method as functions (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over you api logiv',
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})
