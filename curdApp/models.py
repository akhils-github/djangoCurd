from django.db import models


# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    SINO = models.IntegerField()

    def __str__(self):
        return self.name
