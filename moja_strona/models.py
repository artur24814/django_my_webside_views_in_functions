from django.db import models

class Opinion(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    opinion = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    TYPE_DELIVERY = [
        ('-1', 'courier'),
        ('0', 'parcel machine'),
        ('1', 'pick up in person'),
    ]
    name = models.CharField(max_length=64)
    email = models.EmailField()
    adress = models.CharField(max_length=64)
    delivery = models.CharField(max_length=64, choices=TYPE_DELIVERY)
    info_product = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f"/delete_order/{self.id}/"

class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f"/product_info/{self.id}/"

