from django.db import models
from .validators import validataURL
from .utils import createHash
from django.urls import reverse
from django.db.models.signals import post_save

class UrlShortner(models.Model):
    url = models.CharField(max_length=220, validators=[validataURL], unique = True)
    hash = models.CharField(max_length = 8, unique = True, blank = True)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add= True)
    active = models.BooleanField(default = True)
    access_count = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.hash

    def increaseAccessCount(self, *args, **kwargs):
        self.access_count += 1
        self.save()

def save_hash(sender, instance, **kwargs):
    validataURL(instance.url)
    if instance.hash is None or instance.hash == "":
        instance.hash = createHash(instance)
        print(instance.hash, "in save")
        instance.save()
        
    

post_save.connect(save_hash, sender=UrlShortner,
                  dispatch_uid="abc")
