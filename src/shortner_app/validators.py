from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validataURL(url):
    validator = URLValidator()
    # if "http" not in url:
    #     url = 'http://' + url
    try:
        validator(url)
    except:
        raise ValidationError("Invalid URL")
    return url


def checkValidURLs(urlList):
    invalid_urls = []
    validator = URLValidator()
    for url in urlList:
        try:    validator(url)
        except: invalid_urls.append(url)
            
    return invalid_urls
        
    
