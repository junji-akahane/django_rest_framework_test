from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from blog.views import UserViewSet, EntryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
