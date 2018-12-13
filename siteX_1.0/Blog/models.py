from django.db import models

# Create your models here.


class User(models.Model):
	user_ID = models.CharField(max_length=20, primary_key = True)
	user_password = models.CharField( max_length=30 )
	about = models.CharField(max_length=200 )

class Login_info(models.Model):
	username = models.CharField(max_length=20, primary_key =True)
	password = models.CharField(max_length = 30)

class Blog(models.Model):
			blog_ID = models.IntegerField(primary_key = True )
			content = models.CharField(max_length=200)
			user_ID = models.ForeignKey(User, on_delete = models.CASCADE )

class Favorite(models.Model):
			favorite_ID = models.IntegerField(primary_key = True)
			user_ID = models.ForeignKey(User, on_delete = models.CASCADE)
			blog_ID = models.ForeignKey(Blog, on_delete = models.CASCADE)

class Keyword(models.Model):
			keyword_ID = models.IntegerField(primary_key = True)
			keyword = models.CharField(max_length = 200)


class Blog_Keyword(models.Model):
			blog_keyword_ID = models.IntegerField(primary_key = True)
			blog_ID = blog_ID = models.ForeignKey(Blog, on_delete = models.CASCADE)
			keyworkd_ID = models.ForeignKey(Keyword,  on_delete = models.CASCADE)


class Photos(models.Model):
	photo_ID = models.CharField(primary_key = True, max_length = 30)
	pic =  models.ImageField(upload_to = 'Blog/static/Uploaded_Images')
	class Meta:
			db_table = "Photo_db"
