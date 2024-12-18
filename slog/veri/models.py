from django.db import models
import uuid,time
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

def generate_unique_userid():
    timestamp = str(int(time.time()))     
    unique_key = uuid.uuid4().hex[:4]
    user_id = f"USR{timestamp}{unique_key}"
    return user_id

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    usid = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.usid:
            self.usid = generate_unique_userid()

        self.is_active = False

        super().save(*args,**kwargs)
        return self.usid





    
    
class backuser(models.Model):
    userid = models.AutoField
    email = models.EmailField(unique=True,blank=False)
    password = models.CharField(max_length=255,editable=True,blank=False)

    def __str__(self):
        return self.password


