from django.db import models

class Festival(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id}\t{self.name}'


class Film(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    award = models.CharField(max_length=200)
    festival = models.ForeignKey(Festival,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}\t{self.year}\t{self.award}\t{self.festival}'
