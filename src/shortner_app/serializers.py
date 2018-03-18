from rest_framework import serializers
from .models import UrlShortner


class UrlShortnerSerialzers(serializers.ModelSerializer):
    class Meta:
        model = UrlShortner
        fields = "__all__"