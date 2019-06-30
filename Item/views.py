import django_filters
from Item.models import Item
from Item.serializers import ItemSerializer, UserSerializer
from rest_framework import generics
from rest_framework import filters
from rest_framework import permissions
from Item.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User



class ItemFilter(filters.FilterSet):
    min_price = django_filters.NumberFilter(name="PRICE", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="PRICE", lookup_type='lte')
    class Meta:
        model = Item
        fields = ['min_price', 'max_price', 'CATEGORYID','BRANDNAMEID']


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ItemList(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('PRODUCTNAME','PRODUCTNAME')
    ordering_fields = ('PRODUCTNAME', 'PRICE')
    filter_class = ItemFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

