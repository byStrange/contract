from django.db import models
from datetime import timedelta


class Contract(models.Model):
    car_model = models.CharField(max_length=50)
    car_number = models.CharField(max_length=50)
    car_price = models.DecimalField(max_digits=10, decimal_places=0)
    percentage = models.DecimalField(max_digits=5, decimal_places=0)
    length = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    end_date = models.DateField(null=True, blank=True)

    def calculate_end_date(self):
        if self.created_at and self.length:
            self.end_date = self.created_at + timedelta(days=self.length * 30)
            self.save()

    def monthly_payment(self):
        total_price = self.car_price + (self.car_price * self.percentage / 100)
        monthly_payment = total_price / self.length
        return round(monthly_payment, 2)
