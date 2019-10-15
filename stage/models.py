# from django.db import models
# from django.contrib import auth
# from django.contrib.auth.models import User
# # Create your models here.
#
# # class User_Profile(auth.models.User):
#     def __str__(self):
#         return self.user.username
# from django.contrib import auth
# from django.db import models
# from django.utils import timezone
#
#
# class User_Profile(auth.models.User, auth.models.PermissionsMixin):
#     about = models.TextField(null = True)
#     slug = models.SlugField(allow_unicode=True, unique=True)
#
#     def __str__(self):
#         return "@{}".format(self.username)
