from django.db import models

# Create your models here.
class My_User(models.Model):
    username = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.username