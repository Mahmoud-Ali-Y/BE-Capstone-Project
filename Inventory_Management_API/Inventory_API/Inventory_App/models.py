from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='product_added_by', null=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Product_updated_by', null=True)

    def __str__(self):
        return self.name