from django.db import models
from decimal import Decimal

class Car(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    seats = models.IntegerField()
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.name}"

class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # คำนวณยอดเงินอัตโนมัติถ้ายังไม่ได้ถูกส่งมาจาก views
        if self.start_date and self.end_date and self.car:
            days = (self.end_date - self.start_date).days + 1
            if days > 0:
                # สูตร Ferrari Test: 13-17 เม.ย. = 5 วัน
                self.total_price = Decimal(days) * self.car.price_per_day
            else:
                self.total_price = Decimal('0.00')
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_name} - {self.car.name}"