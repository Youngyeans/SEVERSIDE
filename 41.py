from decimal import Decimal
customer = Customer.objects.get(Q(first_name='Manit') | Q(first_name='Senapan'))
order = Order.objects.create(customer=customer, order_date='2024-08-05', remark='ฉันรวย อยากใช้เงินเยอะๆ')
diamond = Product.objects.get(name='Diamond Stud Earrings')
sofa = Product.objects.get(name='Sofa')
rosegold = Product.objects.get(name='Rose Gold Hoop Earrings')

OrderItem.objects.create(order=order, product=diamond, amount=1)
OrderItem.objects.create(order=order, product=sofa, amount=2)
OrderItem.objects.create(order=order, product=rosegold, amount=1)

order_items = OrderItem.objects.filter(order=order)

discount_rate = Decimal('0.10')
total_price = Decimal('0.00')
total_discount = Decimal('0.00')

for obj in order_items:
    product_price = obj.product.price
    obj_total_price = product_price * obj.amount
    obj_discount = obj_total_price * discount_rate
    total_price += obj_total_price - obj_discount
    total_discount += obj_discount

payment = Payment.objects.create(order = order, payment_date = '2024-08-06', remark = 'ลูกค้า VIP ของเรา', price = total_price, discount = total_discount)
for obj in order_items:
    product_price = obj.product.price
    obj_total_price = product_price * obj.amount
    obj_discount = obj_total_price * discount_rate
    PaymentItem.objects.create(payment=payment, order_item=obj, price=obj_total_price, discount=obj_discount)

qr = total_price * Decimal('0.50')
creditcard = total_price - qr

PaymentMethod.objects.create(payment=payment, method="QR", price=qr)
PaymentMethod.objects.create(payment=payment, method="CREDIT", price=creditcard)