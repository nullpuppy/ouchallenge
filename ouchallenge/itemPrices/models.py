from django.db import models


class ItemSale(models.Model):
    title = models.CharField(max_length=120)
    list_price = models.IntegerField()
    sell_price = models.IntegerField()
    city = models.CharField(max_length=120)
    cashless = models.BooleanField()

    def __repr__(self):
        return "<ItemSale: %s, %s, %s, %s, %s>" % (self.title, self.list_price, self.sell_price, self.city, self.cashless)
