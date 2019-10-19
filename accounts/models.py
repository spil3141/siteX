from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.template.defaultfilters import slugify

class UserManager(BaseUserManager):
    def create_user(self, email, password=None,is_active = True, is_staff = False, is_admin = False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError("Users must have a password")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password) #can be used to change user password
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



"""
"password": "pbkdf2_sha256$100000$gT1AEWVp1oYw$j9beOuoOp9XAvycIR21mGGlEg0J1WmXT/G1KyHhOkDQ=",
"last_login": "2019-10-14T15:15:34.522Z",
"is_superuser": false,
"username": "spil3141",
"first_name": "",
"last_name": "",
"email": "",
"is_staff": false,
"is_active": true,
"date_joined": "2019-01-14T06:59:14.239Z",
"groups": [],
"user_permissions": []

"""

class User(AbstractBaseUser):
    username = models.CharField(max_length=100,unique=True)
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255,blank=True,null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    photo = models.ImageField(upload_to="accounts/Profile_Pictures",blank=True)

    about = models.TextField(null=True)
    last_login = models.DateTimeField(auto_now=True,null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects = UserManager()


    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.username)
    #     super(Test, self).save(*args, **kwargs)

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        # return "@{}".format(self.username)
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
