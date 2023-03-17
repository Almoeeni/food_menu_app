from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price= models.IntegerField()
    item_image= models.CharField(max_length=500,default='https://toppng.com/uploads/preview/clipart-free-seaweed-clipart-draw-food-placeholder-11562968708qhzooxrjly.png')
    user = models.ForeignKey(User,on_delete=models.CASCADE , default=1)

    def __str__(self) -> str:
        return self.item_name
    
    def get_absolute_url(self):
        return reverse('food:detail', kwargs={'pk' : self.pk})
