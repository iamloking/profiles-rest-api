from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from profiles_api import models
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        """Returns a list of APIviews features"""
        an_apiview = [
                    'Uses HTTP methods as function (get,post,put,patch,delete)',
                    "Gives you the most control over your app logic",
                    "Is mapped manually to URLS"
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with user's name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message':message})
        else:
            return Response(
                    serializer.errors,
                    status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """Handle partial updating of an object"""
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
