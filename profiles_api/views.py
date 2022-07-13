from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        """Returns a list of APIviews features"""
        an_apiview = [
                    'Uses HTTP methods as function (get,post,put,patch,delete)',
                    "Gives you the most control over your app logic",
                    "Is mapped manually to URLS"
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})
