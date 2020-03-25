from django.db import models
from datetime import datetime
# Create your models here.



class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=400)
    pub_date = models.DateField(default=datetime.now)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name




class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=400, default=" ")

    def __str__(self):
        return self.name