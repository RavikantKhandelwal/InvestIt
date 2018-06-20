from django.db import models
from django.contrib.auth.models import User

class Stocks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    buy_price = models.IntegerField()
    buy_date = models.DateField()
    quantity = models.BigIntegerField();
    total_amount = models.BigIntegerField();
