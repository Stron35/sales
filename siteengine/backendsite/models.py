from django.db import models

# Create your models here.
class Sales(models.Model):
    name = models.TextField()
    price_old = models.FloatField()
    price_new = models.FloatField()
    link = models.TextField()
    image_link = models.TextField()
    date_sale = models.DateField()

    class Meta:
        managed = False
        db_table = 'sales'
