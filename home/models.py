from django.db import models
from django.contrib.auth.models import User

#Create model for Income
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    income_source = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.income_source


#Create model for Expense
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    item = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    def total_expense(self):
        total = self.quantity * self.price
        return total
    
    def __str__(self) -> str:
        return self.item


