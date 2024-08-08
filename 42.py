import json

customer = Customer.objects.get(Q(first_name='Manit') | Q(last_name='Senapan'))
order = Order.objects.get(customer=customer, order_date="2024-08-05")
order_items = OrderItem.objects.filter(order=order)
payment = Payment.objects.get(order=order)
payment_methods = PaymentMethod.objects.filter(payment=payment)

order_data = {
    'order_id': order.id,
    'order_date': order.order_date.isoformat(),
    'order_remark': order.remark,
    'products': [
        {
            'product': item.product.name,
            'amount': item.amount,
            'price': float(item.product.price*item.amount),
            'discount': float((item.product.price*item.amount) * Decimal('0.10'))
        }
        for item in order_items
    ],
    'payment_date': payment.payment_date.isoformat(),
    'payment_remark': payment.remark,
    'payment_method': [
        {
            'method': method.method,
            'price': float(method.price)
        }
        for method in payment_methods
    ]
}

order_json = json.dumps(order_data, ensure_ascii=False, indent=4)
print(order_json)