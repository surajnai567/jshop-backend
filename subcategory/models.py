from django.db import models

# Create your models here.


class SubCategory(models.Model):
    name = models.CharField(max_length=15)
    price = models.FloatField()
    discount = models.IntegerField()

    def __str__(self):
        return self.name
