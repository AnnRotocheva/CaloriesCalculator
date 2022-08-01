from django.db import models
import datetime as dt
from django.utils import timezone


class Product(models.Model):
    name = models.CharField('продукт', max_length = 150)
    calories = models.SmallIntegerField('кКал/г')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Calculator:
    def __init__(self, limit):
        self.records = []
        self.limit = limit

    def add_record(self, record):
        self.record.append(record)

    def get_today_stats(self):
        today = dt.date.today()
        today_stats - sum(record.amount for record in self.records if record.date == today)
        return today_stats

    def remained(self):
        return self.limit - self.get_today_stats()

class Record:
    def __init__(self, amount, comment, date = None):
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.date.today()

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remained = self.remained()
        if calories_remained <= 0:
            return 'На сегодня для организма достаточно, все остальное на вашей совести!'
        return ('Можно съесть что-то еще на {calories_remained} кКал')



