from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=30)
    discriptions = models.CharField(max_length=300)
    day = models.CharField(max_length=15)
    pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.png', verbose_name='pic')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name + ' ' + str(self.price)


class Order(models.Model):
    food = models.OneToOneField(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=300)
    cancelled = models.BooleanField(default=False)

    def __str__(self):
        return self.food.name + ' ' + user.username 

class ExtendUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_chef = models.BooleanField(default=False)
