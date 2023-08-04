from django.db import models
from django.urls import reverse

# A tuple of 2-tuples
LAST_PROPERTY_SIZE= (
    ( 0, 5000 ),
    ( 1, 3000 ),
    (2, 2000)
)

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
  
    def get_absolute_url(self):
        return reverse('detail', kwargs={'builder_id': self.id})
    
class PropertyDetails(models.Model):
    last_built_year = models.IntegerField()
    last_property_size = models.IntegerField(
    choices=LAST_PROPERTY_SIZE,
    default=LAST_PROPERTY_SIZE[0][0])
    last_location = models.CharField(max_length=100)

    builder = models.ForeignKey(Builder, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
      return f"{self.get_last_property_size_display()} sq.ft built in {self.last_built_year} at {self.last_location}  "
    
    