from django.db import models
from django.contrib.auth.models import AbstractUser 
from user.managers import CustomUserManager

GENDER_CHOICES = [ 
    ('M','Male'),
    ('F','Female'),
    ('None','Prefer not to say.'),
]
# Create your models here.
class User(AbstractUser):
    picture=models.ImageField(upload_to='profile_pictures',null=True,blank=True)
    full_name=models.CharField(max_length=50,help_text="Help people discover your account by using the name you're known by : either your full name, nickname, or business name.")
    email=models.EmailField(unique=True)
    #optional Fields
    bio = models.TextField(null=True,blank=True,help_text='Provide your personal information, even if the account is used for a business, a pet or something else. This won\'t be a part of your public profile')
    website = models.URLField(null=True,blank=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES,null=True,blank=True)
    is_private_account = models.BooleanField(null=True,blank=True)
    # to remove these fields from database
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','username']

    objects=CustomUserManager()

    # for name representation in admin panel
    def __str__(self):
        return self.email

    
    
    # to make the property of model so that we able get access in template by dot(.) method
    @property 
    def follower_count(self):
        count = self.follow_followed.count()
        return count

    @property 
    def following_count(self):
        count = self.follow_follower.count()
        return count

    @property 
    def posts_count(self):
        count = self.post_set.count()
        return count

