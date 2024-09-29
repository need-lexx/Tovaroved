import datetime

from django.core.exceptions import ValidationError
from django.utils.timesince import timesince

from .models import Product, CountRecord

def increase_count(product, quantity):
    new_count = product.count + quantity
    if new_count <= 0:
        raise ValidationError("Нельзя увеличить остаток до отрицательного значения")
    product.count = new_count
    product.save()

def decrease_count(product, quantity):
    new_count = product.count - quantity
    if new_count < 0:
        raise ValidationError("Недостаточно товара на складе")
    product.count = new_count
    product.save()

# def record_count_change(product, quantity, action):
#     count_record = CountRecord(product=product, action=action, quantity=quantity)
#     count_record.save()

# def format_count_history(product):
#     history = []
#     for count_record in product.countrecord_set.all():
#         timestamp = datetime.datetime.strftime(count_record.date, '%d-%m-%Y %H:%M:%S')
#         formatted_timestamp = timesince(count_record.date).replace(", ", "")
#         item = f"{count_record.action} {count_record.quantity} шт., {formatted_timestamp} назад."
#         history.append(item)
#     return history