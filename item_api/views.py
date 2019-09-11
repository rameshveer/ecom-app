from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from item_api import serializers

from Item_Management import  Item_Master, Item_Controller
from Item_Management_Srch import Srch_Item_Param, Item_Search


class ItemApiView(APIView):
    """ Test API View"""
    item_get = serializers.Item_Serializer
    item_post = serializers.Item_Post_Serializer

    def get(self, request, format=None):
        item_get_ser = self.item_get(data=request.data)

        if item_get_ser.is_valid():
            item_name = item_get_ser.validated_data.get('item_name')
            item_no = item_get_ser.validated_data.get('item_no')

            #item_nm = f'{item_name}'

            srch1 = Srch_Item_Param(Item_Name =item_name, Item_No =item_no, Item_Brand='')
            srch_result = Item_Search(srch1)

            return Response({'Item Name': item_name, 'data':srch_result})
        else:
            return Response(item_get_ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        item_post_ser = self.item_post(data=request.data)

        if item_post_ser.is_valid():
            item_name = item_post_ser.validated_data.get('item_name')
            item_no = item_post_ser.validated_data.get('item_no')
            item_desc = item_post_ser.validated_data.get('item_desc')
            item_qty = item_post_ser.validated_data.get('item_qty')
            item_brand = item_post_ser.validated_data.get('item_brand')
            item_price = item_post_ser.validated_data.get('item_price')

            item_insert_data = Item_Master(Ino =item_no, Iname=item_name, Idesc=item_desc, Iqty=item_qty, Ibrand=item_brand, Iprice=item_price)

            item_insert = Item_Controller()

            item_insert.Save_ItemMaster(item_insert_data)

            return Response({'Item Insert': 'inserted into ITEM_MASTER Successfully'})
        else:
            return Response(item_post_ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
       """"Handle updating an object"""
       return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
       """Handle a partial update of an object"""
       return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
