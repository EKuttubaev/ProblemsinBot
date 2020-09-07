from peewee import *

db = SqliteDatabase("SKB.db")


class User(Model):
    name = CharField(max_length=20, verbose_name="Ф.И.О")
    created_at = DateTimeField(verbose_name="Дата создания")

    class Meta:
        database = db

class Product(Model):
    price = IntegerField(verbose_name="цена")
    name = CharField(max_length=20, verbose_name="")
    unit = IntegerField(verbose_name="Ед.")
    count = IntegerField(verbose_name="Кол=во")