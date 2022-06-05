from django.db import models
# Create your models here.

class GroceryItem(models.Model):
    item_name=models.CharField(max_length=50)
    item_quantity=models.CharField(max_length=20)
    item_status=models.CharField(max_length=20)
    user_id=models.CharField(max_length=50)
    date=models.DateField()

    def __str__(self):
        return self.item_name
    
