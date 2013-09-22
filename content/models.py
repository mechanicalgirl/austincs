from django.db import models

class Description(models.Model):
    """
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    publish = models.BooleanField(default=False)
    created_at = models.DateField()

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return "/post/%s/" % self.slug

class Activity(models.Model):
    """
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    publish = models.BooleanField(default=False)
    created_at = models.DateField()

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return "/post/%s/" % self.slug

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Activities"
