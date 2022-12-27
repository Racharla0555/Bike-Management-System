from django.db import models

# Create your models here.

# a=(('solved','solved'),('un solved','un solved'))

class Motors(models.Model):
    image=models.ImageField(upload_to='media')
    name=models.CharField(max_length=49)
    model=models.CharField(max_length=30)
    price=models.CharField(max_length=20)
    mileage=models.IntegerField()
    def __str__(self):
        return self.name
