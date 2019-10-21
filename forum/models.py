from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey("accounts.User",related_name="forum_author", on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    star = models.PositiveIntegerField(default = 0)

    # def get_absolute_url(self):
    #     return reverse("Blog:Post_List_Page")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def post_like(self):
        self.star += 1
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey("forum.Post",
                             related_name = "forum_comments",
                             on_delete=models.CASCADE
                             )
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default= timezone.now)

    # def get_absolute_url(self):
    #     return reverse("Blog:Post_List_Page",pk = post.pk)

    def __str__(self):
        return self.author