from rest_framework import viewsets
from .serializers import RealtorSerializer
from .models import Realtor

class RealtorViewSet(viewsets.ModelViewSet):
    queryset = Realtor.objects.all().order_by('name')
    serializer_class = RealtorSerializer