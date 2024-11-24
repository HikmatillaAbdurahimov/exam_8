from django.contrib.auth.backends import UserModel
from django.db import models
from products.models import Products
from django.contrib.auth.models import User


from start.manager import CustomerManager




# class Cart(models.Model):
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         unique_together = (
#             ('product_id', 'user_id'),
#         )
#
#     @property
#     def total_price(self):
#         return self.quantity * self.product.new_price
#
#
#
#
# class Customer(UserModel):
#     objects = CustomerManager()
#
#     class Meta:
#         proxy = True
#
#     def save(self, *args, **kwargs):
#         self.is_customer = True
#         self.is_staff = False
#         self.is_admin = False
#         self.is_superuser = False
#         super().save(*args, **kwargs)

