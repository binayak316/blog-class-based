from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS ={
    (0, "Draft"),
    (1, "Publish")
}
# this makes whether the blog is in draft phase or publishded

class POST(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    Content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
    #     by this desecending order the recently created blog will appear first

    def __str__(self):
        return self.title