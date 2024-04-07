import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, views, status
from rest_framework.response import Response

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

class SampleViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    def list(self, request):  # 引数名を `request` に修正しました
        print('#'*60)
        print('get: request.data: ', request.data)
        print('#'*60)
        all_user_data = User.objects.all()
        serializer = UserSerializer(all_user_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        print('#'*60)
        print('post: request.data: ', request.data)
        print('#'*60)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SampleAPIView(views.APIView):
    def get(self, request):
        all_user_data = User.objects.all()
        serializer = UserSerializer(all_user_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
