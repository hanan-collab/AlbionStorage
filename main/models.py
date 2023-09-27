from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()
    amount = models.IntegerField()
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
