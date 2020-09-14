from datetime import datetime

from peewee import *

db = SqliteDatabase("SKB.db")


class User(Model):
    name = CharField(max_length=20, verbose_name="Ф.И.О")
    created_at = DateTimeField(verbose_name="Дата создания")
    # access = CharField(max_length=10, verbose_name="Доступ")
    tel_id = IntegerField(verbose_name="telegram_id")

    class Meta:
        database = db


db.connect()
db.create_tables([User])


class Product(Model):
    price = IntegerField(verbose_name="Цена")
    name = CharField(max_length=20, verbose_name="Наименование товара")
    unit = IntegerField(verbose_name="Ед. Измерения")
    count = IntegerField(verbose_name="Кол-во")
    total = IntegerField(verbose_name="Итого на сумму")
    date_and_time = DateTimeField(verbose_name="Дата добавления")

    class Meta:
        database = db


db.create_tables([Product])

#total_sum=Product.price*Product.count
#Product.create(price="50", name="Beer", unit="литр", count="10", total="400", date_and_time=datetime.now())
