from django.db import models
from home import models 
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length =200)
    header_image = models.ImageField(null=True,blank=True,upload_to ='images/')
    content =models.TextField()
    date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User,related_name='blog_post')
    @property
    def number_of_comments(self):
        return BlogComment.objects.filter(blogpost = self).count()
    @property
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
       return self.title

    def get_absolute_url(self):
        return reverse('blog-detail',kwargs = {'pk':self.pk})

class BlogComment(models.Model):
  
    name = models.CharField(max_length =500)
    content =models.TextField()
    blogpost =models.ForeignKey(blog,related_name ='comments',on_delete =models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
       return self.blogpost.title[:49]
    def get_absolute_url(self):
       return reverse('add-comment',kwargs = {'pk':self.pk})