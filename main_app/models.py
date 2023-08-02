from django.db import models

# Create your models here.
class Builder(models.Model):
    region=models.CharField(max_length=100)
    house_type=models.CharField(max_length=100)
    rating=models.IntegerField()
    budget_category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    appliances_included=models.BooleanField()


    def __str__(self):
        return ( f'{self.id}| {self.name}')
  