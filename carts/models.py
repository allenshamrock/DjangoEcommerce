from django.db import models
from django.contrib.auth.models import User
from Products.models import Product,Variation 
# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation,blank=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField()

    class Meta:
        unique_together = ('cart','product')
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return self.product.product_name