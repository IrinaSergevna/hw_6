import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from datetime import datetime


class Command(BaseCommand):

    @staticmethod
    def json_read_catalog(): # получаем данные из фикстуры
        with open('catalog.json', 'r', encoding="utf-8") as f:
            return json.load(f)


    def handle(self, *args, **options):

        Product.objects.all().delete() # Удаляем все продукты
        Category.objects.all().delete() # Удаляем все категории


        data = self.json_read_catalog()  # Загружаем данные из JSON-файла
        categories_data = [item for item in data if item['model'] == 'catalog.category'] # Список категорий
        products_data = [item for item in data if item['model'] == 'catalog.product'] # Список продуктов

        # Создаем списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in categories_data:
            category_for_create.append(
                Category(
                    id=category['pk'],
                    name=category['fields']['name'],
                    description=category['fields'].get('description', '')
                        )
                    )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in products_data:
            product_for_create.append(
                Product(
                    id=product['pk'],
                    name=product['fields']['name'],
                    description=product['fields'].get('description', ''),
                    image=product['fields'].get('image', ''),
                    category=Category.objects.get(id=product['fields']['category']),
                    price=product['fields'].get('price', 0),
                    created_at=parse_datetime(product['fields']['created_at']),
                    updated_at=parse_datetime(product['fields']['updated_at'])
                )
            )


        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)

        self.stdout.write(self.style.SUCCESS("Данные успешно загружены в базу данных."))

