from django.db import models

# Create your models here.

class Previl(models.Model):
    usage=models.CharField(max_length=50)
    plan=models.CharField(max_length=50)

    def __str__(self):
        return self.plan
        
    
class user(models.Model):
    fullname=models.CharField(max_length=100)
    user_id=models.CharField(max_length=3)
    mobile=models.CharField(max_length=15)
    previl=models.ForeignKey(Previl,on_delete=models.CASCADE)

class UserActivity(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    activity = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)


class clients(models.Model):
    cli=models.CharField(max_length=50)

    def __str__(self):
        return self.cli
