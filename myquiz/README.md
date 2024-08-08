# WEEK 6 QUIZ

## Instruction

1. สร้าง `virtual environment`
2. ติดตั้ง `django` และ `psycopg2` libraries
3. สร้างโปรเจคใหม่ใหม่ชื่อ`myservice`
4. จากนั้นให้ทำการ startapp ใหม่ชื่อ `service`
5. สร้าง database ชื่อ `service` ใน Postgres DB
6. ทำการเพิ่ม code ด้านล่างนี้ในไฟล์ `service/models.py`
7. เพิ่ม **'service'** ใน `settings.py`
8. ทำการ `makemigrations` และ `migrate`
9. import ข้อมูลจาก `service.sql` ลงไปใน database

```python
from django.db import models
from django.contrib.auth.models import User

# Extend the User model to include ServiceProviders
class ServiceProvider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name

# Service model to represent different services offered by the service providers
class Service(models.Model):
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} by {self.service_provider.name}"

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name

# New Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name

# Appointment model to represent appointments booked by users
class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment of {self.customer.name} with {self.service.service_provider.name} on {self.appointment_date} at {self.appointment_time}"
```

10. จากนั้นทำการติดตั้งเพื่อใช้งาน jupyter notebook ตามขั้นตอนใน `django_notebook.md`
11. เริ่มทำ QUIZ ได้เลย
