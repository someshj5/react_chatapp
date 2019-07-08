from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=255,default='username')
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)




