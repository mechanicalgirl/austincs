from django.db import models

AVAILABILITY_CHOICES = (
    ('A', 'Only one time during the school year'),
    ('B', 'Several times during the year'),
    ('C', 'Once a month'),
    ('D', 'Weekly'),
)

class Developer(models.Model):
    """
    Developers - Austin CSTA volunteer program sign-ups
    """
    name = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=200, blank=False, unique=True,
            verbose_name='Email Address')
    bio = models.CharField(max_length=200, blank=False,
            help_text='What languages do you work in?  What are your areas of \
            programming expertise?')
    availability = models.CharField(max_length=1, blank=False,
            choices=AVAILABILITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % (self.name)
