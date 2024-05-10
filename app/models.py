from django.db import models
from django.contrib.auth.models import User

# User=get_user_model()
# Create your models here.

class students(models.Model):
    name=models.CharField(max_length=22)
    age=models.IntegerField(default=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='createdBy')
    updatedBy=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='updatedBy')


    def __str__(self):
        return self.name
