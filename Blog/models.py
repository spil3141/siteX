from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.



class Post(models.Model):
    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # star = models.ManyToManyField("accounts.User",related_name="blog_likes")

    def get_absolute_url(self):
        return reverse("Blog:Post_List_Page")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # def list_of_users_that_liked_this_post(self):
    #     return self.star.all()


    def approved_comments(self):
        return self.comments.filter(approved_comment = True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey("Blog.Post",
                             related_name = "comments",
                             on_delete=models.CASCADE
                             )
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default= timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("Blog:Post_List_Page",pk = post.pk)

    def __str__(self):
        return self.author
