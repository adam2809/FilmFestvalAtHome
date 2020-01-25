from django.db import models

class Festival(models.Model):
    name = models.CharField(max_length=200)

    
class Film(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    award = models.CharField(max_length=200)
    festival = models.ForeignKey(Festival,on_delete=models.CASCADE)
