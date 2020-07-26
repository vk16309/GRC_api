from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,first_name,last_name,dob,department,city,state,institute,enrollment_no,contact_no,upload_id,category,password=None):
        '''create a new user profile'''
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name,last_name=last_name,dob=dob,department=department,city=city,
                            state=state,institute=institute,enrollment_no=enrollment_no,contact_no=contact_no,upload_id=upload_id,category=category)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,dob,first_name,last_name,password):
         '''Create and save a new superuser with given details'''
         user = self.create_user(email=email, first_name=first_name,last_name=last_name,dob=dob,department='',city='',state='',institute='',enrollment_no=0,contact_no=0,upload_id=None,category=None,password=password)

         user.is_superuser = True
         user.is_staff = True
         user.save(using=self._db)

         return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    CHOICES1 = [
        ('11', 'Department'),
        ('12', 'Institute/College'),
        ('13', 'University'),
    ]
    CHOICES2 = [
        ('11', 'Admission'),
        ('12', 'Finance'),
        ('13', 'Examination'),
        ('21', 'Lecture TimeTable/ Learning'),
        ('22', 'Paper Re-evaluation'),
        ('31', 'Others'),
    ]
    """Database model for user in the system"""
    email = models.EmailField(max_length=255,unique=True)
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    dob=models.DateField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    institute=models.CharField(max_length=60)
    department=models.CharField(max_length=20,null=True,blank=False)
    enrollment_no=models.IntegerField()
    contact_no=models.IntegerField()
    upload_id=models.ImageField(upload_to='media/id',blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_redressal = models.BooleanField(default=False)
    category =models.CharField(max_length=30,choices = CHOICES1,null=True)
    sub_category = models.CharField(max_length=30,choices=CHOICES2,null=True)
    #############################
    # email_confirmed = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['first_name','last_name','dob','address','city','state','institute','enrollment_no','contact_no','upload_id']
    REQUIRED_FIELDS = ['first_name','last_name','dob']

    def get_full_name(self):
        ''' Retrieve Full Name of the User '''
        return (self.first_name +" "+ self.last_name)

    def get_short_name(self):
        """Retrieve short name of user"""

        return self.first_name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class Complaint(models.Model):
    """Complaint model for student"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        )    
    institute_name=models.CharField(max_length=60,null=True)    
    category=models.CharField(max_length=50,blank=False)
    sub_category=models.CharField(max_length=50,blank=False)
    complaint_text=models.TextField(blank=False)
    subject=models.CharField(max_length=100,null=True,blank=False)
    status = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    upload_file=models.FileField(upload_to='media/docs',null=True,blank=True)

    def __str__(self):
        return self.category
