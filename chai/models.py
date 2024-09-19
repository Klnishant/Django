from django.db import models
from datetype import DateTime
from django.contrib.auth.models import User

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
    
class chaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety,on_delete=models.CASCADE,related_name='review')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=DateTime.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
        

class Stores(models.Model):
    chai_variety = models.ManyToManyField(ChaiVariety,related_name='stores')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=DateTime.now)
    valid_till = models.DateTimeField()

    def __str__(self):
        return f'certificate for {self.chai.name}'