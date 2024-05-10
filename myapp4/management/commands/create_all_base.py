from django.core.management.base import BaseCommand
from myapp4_app.models import Order, Client, Product
from django.utils.crypto import get_random_string
from django.utils.timezone import now
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Populate the database with sample orders and related data'

    def handle(self, *args, **options):
        # Создаем несколько клиентов
        clients = [Client.objects.create(
            name=f'Client {i}',
            email=f'client{i}@example.com',
            phone_number=f'12345678{i}',
            address=f'Street {i}'
        ) for i in range(1, 6)]

        # Создаем несколько товаров
        products = [Product.objects.create(
            name=f'Product {i}',
            description=f'Description for Product {i}',
            price=Decimal(random.uniform(10, 100)),
            quantity=random.randint(1, 10)
        ) for i in range(1, 11)]

        # Создаем несколько заказов и связанных продуктов
        for i in range(1, 6):
            client = random.choice(clients)
            products_in_order = random.sample(products, random.randint(1, 5))
            total_amount = sum(product.price * product.quantity for product in products_in_order)
            order = Order.objects.create(
                client=client,
                total_amount=total_amount,
                order_date=now()
            )
            order.products.set(products_in_order)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample orders.'))