from django.db import models


# Create your models here.

class Trypincode(models.Model):
    pincode = models.IntegerField(default=123456)
    authcode = models.CharField(max_length=200,default="9o5p5d51kcjhx1zn3ry16tgpxys5muj64clu2wgf0rbmj2rj0wsmmo3jx116xhkjxa6matc5ks8f41cbl4dv0fa7zb6tk8mplrdygk3kzbr9pomjaw19g2u1h4d58r9b")
    email = models.EmailField(max_length=100)
    pwd = models.CharField(max_length=100)
    techID = models.IntegerField(default=1234567)
    channel = models.CharField(max_length=200,default='CHANNEL01')
def __str__(self):
    return self.authcode