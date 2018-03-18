from rest_framework.views import APIView
from .serializers import UrlShortnerSerialzers
from .models import UrlShortner


class ShortenApiMixin(APIView):
    serializer_class = UrlShortnerSerialzers

    @staticmethod
    def get_or_create(long_url):
        try:
            return UrlShortner.objects.get(url=long_url, active=True)
        except UrlShortner.DoesNotExist:
            object = UrlShortner.objects.create(url=long_url)
            return object
            
    @staticmethod
    def get_object(hash):
        try:
            return UrlShortner.objects.get(hash=hash, active=True)
        except UrlShortner.DoesNotExist:
            return False



            
            
