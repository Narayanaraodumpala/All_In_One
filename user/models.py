from statistics import mode
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserData(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    mobile = models.IntegerField()
    image = models.ImageField(upload_to='media/', null=True)
    unique_user_id=models.CharField(max_length=10,null=True)
    forgot_password_token=models.CharField(max_length=100,null=True)

    class Meta:
        db_table='Users'

    def __str__(self):
        return self.user.username


