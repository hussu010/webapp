from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Level(models.Model):
    level = models.CharField(max_length=20)
    def __str__(self):
        return self.level

class Subject(models.Model):
    subject = models.CharField(max_length=20)
    def __str__(self):
        return self.subject

class Post(models.Model):
    title       = models.CharField(max_length=100)
    content     = models.TextField()
    overview = models.TextField()
    updated     = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp   = models.DateTimeField(auto_now=False,auto_now_add=True)
    slug        = models.SlugField(unique=True, blank=False)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

def create_slug(instance, new_slug = None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s"%(slug, qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug= create_slug(instance)

pre_save.connect(pre_save_post_receiver,sender=Post)

