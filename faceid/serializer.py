from .models import Image
from rest_framework import serializers


class Imageserializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'name', 'photo', 'created']

