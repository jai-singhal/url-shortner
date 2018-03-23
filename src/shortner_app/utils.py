import random
import string

def createHash(instance, max_size=8):
    charRange = string.ascii_lowercase + string.digits #+ string.ascii_uppercase
    newHash = ''.join(random.choice(charRange) for _ in range(max_size))
    Klass = instance.__class__
    qs = Klass.objects.filter(hash=newHash)
    if qs.exists():
        createHash(instance, max_size=max_size)
    return newHash

