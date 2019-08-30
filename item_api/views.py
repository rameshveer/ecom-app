from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from item_api import serializers

from Item_Management_Srch import Srch_Item_Param, Item_Search


class ItemApiView(APIView):
    """ Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """" Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            item = f'{name}'
            srch1 = Srch_Item_Param(Item_Name =item, Item_No ='3', Item_Brand='')
            srch_result = Item_Search(srch1)

            return Response({'message': item, 'data':srch_result})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
       """"Handle updating an object"""
       return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
       """Handle a partial update of an object"""
       return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
