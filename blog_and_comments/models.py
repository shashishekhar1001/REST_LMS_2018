from django.db import models
from registration.models import Custom_User
from django.core.urlresolvers import reverse
# Create your models here.

class Blog(models.Model):
    blogger = models.ForeignKey(Custom_User)
    title = models.CharField(max_length=120)
    # slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='blog_pics/%Y/%m/%d/', blank=True)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    likes = models.ManyToManyField(Custom_User, related_name='blog_likes', blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("view_blog", kwargs={"id": self.id})

    def get_like_url(self):
        return reverse("like_toggle", kwargs={"id": self.id})

    def get_api_like_url(self):
        return reverse("api_like_toggle", kwargs={"id": self.id})

    class Meta:
        ordering = ["-created", "-updated"]