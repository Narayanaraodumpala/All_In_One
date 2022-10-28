import email
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dashboard(models.Model):
      id=models.CharField(max_length=20,primary_key=True)
      dashboard_type=models.CharField(max_length=20)

      def __str__(self):
          return self.dashboard_type

      class Meta:
          db_table='Dashboard Types'



class FeedBack(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    feedback=models.CharField(max_length=10)
    suggestion=models.CharField(max_length=750)

    def __str__(self):
        return self.name


    class Meta:
        db_table='FeedBack'
