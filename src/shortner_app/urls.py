from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import (
    ShortenSingleApiView,
    FetchLongUrlApiView,
    ShortenMultiApiView,
    FetchLongListUrlApiView,
    shortURLView,
    FetchAccessCountView,
    cleanURLS,
)

urlpatterns = [
    re_path('fetch/short-url/', ShortenSingleApiView.as_view()),
    re_path('fetch/short-urls/', ShortenMultiApiView.as_view()),
   
    re_path('fetch/long-url/', FetchLongUrlApiView.as_view()),
    re_path('fetch/long-urls/', FetchLongListUrlApiView.as_view()),

    re_path('fetch/count/', FetchAccessCountView.as_view()),
    
    re_path('clean-urls/', cleanURLS),
    
    path('', TemplateView.as_view(template_name="index.html")),
    re_path('(?P<hash>[a-z0-9]{1,8})', shortURLView),
    
    
    
]
