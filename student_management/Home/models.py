from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    usertype=models.CharField(max_length=15)
    department=models.CharField(max_length=15)
    phone=models.BigIntegerField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)




class Teacher(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    experience=models.IntegerField()
    salary=models.BigIntegerField()

