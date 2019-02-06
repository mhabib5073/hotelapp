from django.db import models
from django.urls import reverse


class Manager(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=25)
    booking = models.CharField(max_length=25)
    def __str__(self):
        return self.booking

class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.CharField(max_length=25)
    address = models.CharField(max_length=50, null=True)
    date = models.DateTimeField()
    booking= models.ForeignKey(Manager,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('HotalApp:index')


