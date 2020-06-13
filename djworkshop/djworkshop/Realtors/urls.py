
from django.urls import include, path
from rest_framework import routers
from . import api_view

router = routers.DefaultRouter()
router.register(r'v1', api_view.RealtorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]