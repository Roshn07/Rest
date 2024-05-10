from django.db import models

# Create your models here.


class subject(models.Model):
    name=models.CharField(max_length=20)


    def __str__(self):
        return self.name
    
class student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(default=10)
    choices=(('male','m'),('female','f'))
    gender=models.CharField(choices=choices,max_length=20)


    def __str__(self):
        return self.name