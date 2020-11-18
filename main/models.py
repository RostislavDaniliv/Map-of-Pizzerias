from django.contrib.gis.db import models


class Pizzerias(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    coordinates = models.PointField(null=True, blank=True)

    def __str__(self):
        return self.name