from django.db import models

from developer.models import Developer
from teacher.models import Teacher

class Match(models.Model):
    developer = models.ForeignKey(Developer)
    teacher = models.ForeignKey(Teacher)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"Teacher: %s - Developer: %s" % (self.teacher, self.developer)

    class Meta:
        verbose_name_plural = "Matches"
