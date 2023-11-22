import peewee

db = peewee.SqliteDatabase("database.db")

class User(peewee.Model):
    name = peewee.CharField()
    address = peewee.CharField()
    billing = peewee.CharField()

    class Meta:
        database = db

class Product(peewee.Model):
    product = peewee.CharField()
    description = peewee.CharField()
    tags = peewee.CharField()
    price = peewee.DecimalField()
    amount = peewee.IntegerField()
    user_id = peewee.ForeignKeyField(User,backref='products')

    class Meta:
        database = db


class Transaction(peewee.Model):

    buyer_id = peewee.IntegerField()
    seller_id = peewee.IntegerField()
    product_name = peewee.CharField()
    amount = peewee.IntegerField()
    transaction_date = peewee.DateTimeField()

    class Meta:
        database = db