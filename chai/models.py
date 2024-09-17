from django.db import models
from datetype import DateTime

# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML','Masala'),
        ('GR','Ginger'),
        ('KL','Kiwi'),
        ('PL','Plain'),
        ('EL','Elaichi'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateField(default=DateTime.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICES,default='ML')
    description = models.TextField(default='')

    def __str__(self):
        return self.name