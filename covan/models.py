from django.db import models

# Create your models here.



class data(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=20)
    mono=models.IntegerField(default='')


    def __str__(self):
        return self.name

    