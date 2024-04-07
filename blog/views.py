import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EntryFilter(django_filters.FilterSet):
    author = django_filters.NumberFilter()
    status = django_filters.CharFilter()

    class Meta:
        model = Entry
        fields = ('author', 'status')

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EntryFilter
