from rest_framework import serializers
from .models import Desc

class DescSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Desc
        fields = ('title','price','option')
