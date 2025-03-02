from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

# User=get_user_model()

class User(AbstractUser):
    is_organisor=models.BooleanField(default=True)
    is_agent=models.BooleanField(default=False)

class UserProfile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):

    # values stored in (database ,diplay value) , does not restrict the value can also stroe a  different value


    # SOURCE_CHOICES=(
    #     ('youtube','youtube'),
    #     ('google','google'),
    #     ('newsletter','newsletter')

    # )

    first_name = models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    agent=models.ForeignKey("Agent",null=True,blank=True, on_delete=models.SET_NULL)
    organisation=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    category=models.ForeignKey("Category" ,related_name="leads",null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # agent can be put in quotation and then it would not benecessary to be put in top , 
    # if you just write agent then you would hgave to put theagent calss on the top
    
    # phoned=models.BooleanField(default=False)
    # source=models.CharField(choices=SOURCE_CHOICES)

    # profile_pic=models.ImageField(blank=True,null=True)

    # special_file=models.FileField()

class Agent(models.Model):

    # user=models.ForeignKey(User,on_delete=models.CASCADE)

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    organisation=models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    
  
class Category(models.Model):
    name=models.CharField(max_length=30)
    organisation=models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    



@receiver(post_save, sender=User)
def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        
        UserProfile.objects.create(user=instance)
    