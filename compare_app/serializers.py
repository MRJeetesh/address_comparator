from rest_framework import serializers

class AddressCompareSerializer(serializers.Serializer):
    address1 = serializers.CharField()
    address2 = serializers.CharField()

    
