from django.db import models

# Create your models here.
class ticket(models.Model):
    First_Name = models.CharField(max_length=15)
    Last_Name = models.CharField(max_length=15)
    From = models.CharField(max_length=10)
    To = models.CharField(max_length=10)
    Mob = models.IntegerField()
    Flight_Date = models.CharField(max_length=15)
    Class = models.CharField(max_length=20)

    def __str__(self):
        return self.First_Name       

