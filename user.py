from peewee import *
from datetime import date

db = SqliteDatabase("SKB.db")


class User(Model):
    name = CharField(max_length=20, verbose_name="Ф.И.О")
    created_at = DateTimeField(verbose_name="Дата создания")
    access = CharField(max_length=10, verbose_name="Доступ")

    class Meta:
        database = db


class Product(Model):
    name = CharField(max_length=20, verbose_name="Наименование товара")
    price = IntegerField(verbose_name="Цена")
    unit = IntegerField(verbose_name="Ед. Измерения")
    count = IntegerField(verbose_name="Кол-во")

    class Meta:
        database = db

db.connect()


db.create_tables([User, Product])

