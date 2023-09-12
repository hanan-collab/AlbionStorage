from django.db import models

class Product(models.Model):
    accountID = models.CharField(max_length=255)
    balance = models.IntegerField()
    # date_added = models.DateField(auto_now_add=True)
    item = models.CharField(max_length=255)
    description = models.TextField()
    itemPower = models.IntegerField()
    tier = models.IntegerField()
    amount = models.IntegerField()
    place = models.CharField(max_length=255)
    price = models.IntegerField()