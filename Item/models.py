from django.db import models


class Item(models.Model):


    PRODUCTNAME = models.CharField(max_length=100)
    BRANDNAMEID = models.BigIntegerField(null=True)
    CATEGORYID = models.BigIntegerField(null=True)
    SMURL = models.URLField(null=True)
    COVERURL= models.URLField(null=True)
    PRICE = models.DecimalField(max_digits=5, decimal_places=2)
    DETAILS=models.TextField()
    owner = models.ForeignKey('auth.User', related_name='Item', null=True)

