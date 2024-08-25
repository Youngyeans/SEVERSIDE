from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    address = models.JSONField(null=True)

class Cart(models.Model):
    customer = models.ForeignKey("shop.Customer", on_delete=models.PROTECT)
    create_date = models.DateTimeField()
    expired_in = models.IntegerField(default=60)

class CartItem(models.Model):
    cart = models.ForeignKey("shop.Cart", on_delete=models.PROTECT)
    product = models.ForeignKey("shop.Product", on_delete=models.PROTECT)
    amount = models.IntegerField(default=1)

class Order(models.Model):
    customer = models.ForeignKey("shop.Customer", on_delete=models.PROTECT)
    order_date = models.DateField()
    remark = models.TextField(null=True)

class OrderItem(models.Model):
    order = models.ForeignKey("shop.Order", on_delete=models.PROTECT)
    product = models.ForeignKey("shop.Product", on_delete=models.PROTECT)
    amount = models.IntegerField(default=1)

class ProductCategory(models.Model):
    name = models.CharField(max_length=150)

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    remaining_amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField("shop.ProductCategory")

class Payment(models.Model):
    order = models.OneToOneField("shop.Order", on_delete=models.CASCADE, primary_key=True)
    payment_date = models.DateField()
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class PaymentMethod(models.Model):
    payment = models.ForeignKey("shop.Payment", on_delete=models.CASCADE)
    qr= "QR"
    credit= "CREDIT"
    method_choices = {
        qr: "QR",
        credit: "CREDIT",
    }
    method = models.CharField(
        choices=method_choices,
        default=qr,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

class PaymentItem(models.Model):
    payment = models.ForeignKey("shop.Payment", on_delete=models.CASCADE)
    order_item = models.OneToOneField("shop.OrderItem", on_delete=models.CASCADE, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)