from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    designation = models.CharField(max_length=20,null=False)
    salary = models.IntegerField(null=True,blank=True)

    # class Meta:
    #     ordering = ('salary')

    def __str__(self):
        return "{0} {1}" . format(self.user.first_name , self.user.last_name)

@receiver(post_save,sender=User)
def user_is_created(sender,instance,created,**kwargs):
    print("senderrrrrr" , sender)
    print("instanceeee" , instance)
    print("createddddd" , created)
    print("kwargssssss" , kwargs)
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()