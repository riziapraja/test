from rest_framework import viewsets
from .serializers import DescSerializer
from .models import Desc

class DescViewSet(viewsets.ModelViewSet):
    queryset = Desc.objects.all().order_by('title')
    serializer_class = DescSerializer
