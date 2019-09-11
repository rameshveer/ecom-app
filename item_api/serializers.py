from rest_framework import serializers


class Item_Serializer(serializers.Serializer):
    """Serializes a fields our APIView"""
    item_name   = serializers.CharField(max_length=10)
    item_no     = serializers.CharField(max_length=10)

class Item_Post_Serializer(serializers.Serializer):
    """Serializes a fields our APIView"""
    item_name   = serializers.CharField(max_length=10)
    item_no     = serializers.CharField(max_length=10)
    item_desc   = serializers.CharField(max_length=50)
    item_qty    = serializers.IntegerField(max_value=10000, min_value=1)
    item_brand  = serializers.CharField(max_length=20)
    item_price  = serializers.DecimalField(max_digits=9, decimal_places=2)
