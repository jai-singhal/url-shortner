from django.urls import path, re_path
from .views import (
    ShortenSingleApiView,
    FetchLongUrlApiView,
    ShortenMultiApiView,
    FetchLongListUrlApiView,
    shortURLView,
    FetchAccessCountView,
    cleanURLS
)

urlpatterns = [
    re_path('fetch/short-url/', ShortenSingleApiView.as_view()),
    re_path('fetch/short-urls/', ShortenMultiApiView.as_view()),
   
    re_path('fetch/long-url/', FetchLongUrlApiView.as_view()),
    re_path('fetch/long-urls/', FetchLongListUrlApiView.as_view()),

    re_path('fetch/count/', FetchAccessCountView.as_view()),
    
    re_path('clean-urls/', cleanURLS),
    
    re_path('(?P<hash>[a-z0-9]{1,8})', shortURLView),
    
    
    
]
