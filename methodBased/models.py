from django.db import models



class Buildings(models.Model):    
    region = models.CharField( max_length = 20)
    zone = models.CharField(max_length=30)
    buildingName = models.CharField(max_length=30)
    buildingCode = models.CharField(max_length=30)
    mtrNo = models.CharField(max_length=30)
    token = models.CharField(max_length=30)
    revenue = models.CharField(max_length=30)


    def __str__(self):
        return self.buildingName +self.buildingCode