
from django.db import models
from django.urls import reverse

class Product(models.Model):
    title  = models.CharField(max_length = 200)
    designer_name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500, default=None)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length = 2083, default=False)
    follow_designer = models.CharField(max_length=2083, blank=True)  
    product_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Order(models.Model):
	product = models.ForeignKey(Product, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.title
