from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.db.models.signals import post_save

# Create your models here(object):

GENDER = (
    ('','select'),
    ('Female','Female'),
    ('Male','Male'),
)

SEM={
	('','select'),
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('5','5'),
	('6','6'),
	('7','7'),
	('8','8'),
}

# ------------------------------------------------------------------------------------------------
class Profile (models.Model):
    user            = models.OneToOneField(User,verbose_name="User", on_delete=models.CASCADE,null=True)
    name            = models.CharField(verbose_name="Name",max_length=60,null=True)
    email           = models.EmailField(max_length=50,null=True)
    u_roll          = models.PositiveIntegerField(verbose_name="University Roll no.",null=True)
    city            = models.CharField(verbose_name="City", max_length=50,null=True)
    sem             = models.CharField(verbose_name="Semester",choices=SEM,null=True,max_length=1)
    gender          = models.CharField(verbose_name="Gender", default = 'Male', max_length=50,choices = GENDER,null=True)
    addess          = models.CharField(verbose_name="Address", max_length=50,null=True)
    birth_date      = models.DateField(("Date of birth"), default=datetime.date.today,null=True)
    ditrict         = models.CharField(verbose_name="District",max_length=50,null=True)
    pin             = models.PositiveIntegerField(verbose_name="Pin",null=True)
    contact         = models.PositiveIntegerField(verbose_name="Contact",null=True)
    
    def __str__(self):
        return f'{self.user.email}'

#   --------------------------------------------------------------------------------------------------------------  # 
def create_profile(sender, **kwargs):
    if(kwargs["created"]):
        user_profile = Profile.objects.create(user = kwargs["instance"])

post_save.connect(create_profile,sender=User)


class Internship(models.Model):
    #notice added day
    head          = models.CharField(max_length=100,null=True)
    body          = models.TextField(max_length=10000,null=True)
    starting_date = models.DateField(default=datetime.date.today,null=True)
    ending_date   = models.DateField(default=datetime.date.today,null=True)

    def __str__(self):
        return f'{self.head}'

class Jobs(models.Model):
    #notice added day
    head          = models.CharField(max_length=100,null=True)
    body          = models.CharField(max_length=500,null=True)
    starting_date = models.DateField(default=datetime.date.today,null=True)
    ending_date   = models.DateField(default=datetime.date.today,null=True)

    def __str__(self):
        return f'{self.head}'

        


