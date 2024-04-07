from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from blog.views import UserViewSet, EntryViewSet, SampleViewSet, SampleAPIView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'all_users', SampleViewSet, basename='all_users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/all_users2/', SampleAPIView.as_view(), name='sample_api'),  # APIViewに変更    
]

