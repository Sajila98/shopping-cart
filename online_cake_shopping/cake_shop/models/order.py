from django.db import models

STATUS_CHOICE = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)


class OrderDetails(models.Model):
    user = models.IntegerField(default=True)
    product_name =models.CharField(max_length=250)
    image = models.ImageField(null=True,blank=True)
    qty =models.PositiveIntegerField(default=1)
    price =models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,default='pending',choices=STATUS_CHOICE)