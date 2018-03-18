from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from .models import UrlShortner
from .validators import validataURL, checkValidURLs
from .mixins import ShortenApiMixin
from django.views.decorators.csrf import csrf_exempt
import json


class ShortenSingleApiView(ShortenApiMixin):
    def post(self, request, *args, **kwargs):
        long_url = self.request.data['long_url']
        try:
            object = self.get_or_create(long_url)
            short_uri = request.get_host() + "/" + object.hash

            data = {
                "short_url": short_uri,
                "status": "OK",
                "status_codes": []
            }
            status_code = status.HTTP_200_OK
        except:
            data = {
                "status": "FAILED",
                "status_codes": ["INVALID_URLS"]
            }
            status_code = status.HTTP_400_BAD_REQUEST
        
        return Response(data, status=status_code)


class FetchLongUrlApiView(ShortenApiMixin):
    def post(self, request, *args, **kwargs):
        short_url = self.request.data['short_url'].split('/')[-1]
        instance = self.get_object(short_url)
        if instance:
            data = {
                "long_url": instance.url,
                "status": "OK",
                "status_codes": []
            }
            status_code = status.HTTP_200_OK
        else:
            data = {
                "status": "FAILED",
                "status_codes": ["INVALID_URLS"]
            }
            status_code = status.HTTP_400_BAD_REQUEST

        return Response(data, status=status_code)


class ShortenMultiApiView(ShortenApiMixin):
    def post(self, request, *args, **kwargs):
        long_urls = self.request.data['long_urls']
        valid_urls = {}
        invalid_urls = checkValidURLs(long_urls)
        if len(invalid_urls) == 0:
            for url in long_urls:
                object = self.get_or_create(url)
                short_uri = request.get_host() + "/" + object.hash
                valid_urls[url] = short_uri

                data = {
                    "short_urls": valid_urls,
                    "invalid_urls": [],
                    "status": "OK",
                    "status_codes": []
                }
                status_code = status.HTTP_200_OK
        else:
            data = {
                "invalid_urls": invalid_urls,
                "status": "FAILED",
                "status_codes": ["INVALID_URLS"]
            }
            status_code = status.HTTP_400_BAD_REQUEST

        return Response(data, status=status_code)


class FetchLongListUrlApiView(ShortenApiMixin):
    def post(self, request, *args, **kwargs):
        short_urls = self.request.data['short_urls']
        valid_urls = {}
        invalid_urls = []
        for url in short_urls:
            hash = url.split("/")[-1]
            instance = self.get_object(hash)
            if not instance:
                invalid_urls.append(url)
            else:
                valid_urls[url] = instance.url
            
        if not invalid_urls:
            data = {
                "long_urls": valid_urls,
                "invalid_urls": [],
                "status": "OK",
                "status_codes": []
            }
            status_code = status.HTTP_200_OK
        else:
            data = {
                "status": "FAILED",
                "invalid_urls": invalid_urls,
                "status_codes": ["INVALID_URLS"]
            }
            status_code = status.HTTP_400_BAD_REQUEST

        return Response(data, status=status_code)


def shortURLView(request, hash):
    instance = get_object_or_404(UrlShortner, hash = hash)
    instance.increaseAccessCount()
    return HttpResponseRedirect(instance.url)


class FetchAccessCountView(APIView):
    def post(self, request, *args, **kwargs):
        short_url = self.request.data['short_url']
        hash = short_url.split("/")[-1]
        qs = UrlShortner.objects.filter(hash=hash)
        if qs.exists():
            instance = UrlShortner.objects.get(hash=hash)
            data = {
                "count": instance.access_count,
                "status": "OK",
                "status_codes": []
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                "status": "FAILED",
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    

@csrf_exempt
def cleanURLS(request):
    UrlShortner.objects.all().delete()
    return JsonResponse({"status": "OK"}, status=200)
    
