from django.db import models
from django.contrib.auth.models import AbstractUser, User, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class User(AbstractUser):
	is_customer = models.BooleanField(default=False)
	is_mechanic = models.BooleanField(default=False)
	fullname = models.CharField(max_length=100)
	workshop = models.CharField(max_length=100)
	special = models.CharField(max_length=100, default="nothing")
	location = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	contact = models.CharField(max_length=12)
	bio = models.TextField(default="hi")

#class Customer(AbstractBaseUser):
#	fullname = models.CharField(max_length=100)
#	location = models.CharField(max_length=50)
#	city = models.CharField(max_length=50)
#	contact = models.CharField(max_length=12)
#	REQUIRED_FIELDS = ['contact']



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=100)
	email = models.EmailField(max_length=50)
	workshop = models.CharField(max_length=100)
	special = models.CharField(max_length=100, default="nothing")
	location = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	contact = models.CharField(max_length=12)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	bio = models.TextField(default="hi")

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
