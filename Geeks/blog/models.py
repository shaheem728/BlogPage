from asyncio.windows_events import NULL
from  pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.text import slugify
# Create your models here.
class Post(models.Model):
    Sno = models.AutoField(primary_key=True)
    slug = models.SlugField(unique=True)
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=150)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    content=models.TextField()

    def __str__(self):
        return f"Posted by {self.author} - {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # This automatically replaces spaces with hyphens
        super(Post, self).save(*args, **kwargs)    
    
class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(default=now)
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"



  