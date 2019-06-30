from rest_framework import serializers
from Item.models import Item
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id','PRODUCTNAME', 'BRANDNAMEID', 'CATEGORYID', 'SMURL', 'COVERURL','PRICE', 'DETAILS')


class UserSerializer(serializers.ModelSerializer):
    Item = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username','Item')

