from django.db import models

class Needs(models.Model):
    description = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Needs"

    def __unicode__(self):
        return u"%s" % (self.description)

class Teacher(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=200, blank=False, unique=True,
            verbose_name='Email Address')
    school = models.CharField(max_length=200, blank=False,
            verbose_name='At which school do you teach?')
    school_zip_code = models.CharField(max_length=10, blank=False,
            verbose_name="What is the school's zip code? (for pairing purposes")
    grade_age = models.CharField(max_length=10, blank=False,
            verbose_name='What grade/age group do you teach?')
    no_of_students = models.CharField(max_length=4, blank=False,
            verbose_name='How many students?')
    needs = models.ManyToManyField(Needs, blank=False, help_text='What kinds of \
            participation from a member of the local programming community would \
            you like to see in your classroom?')
    other = models.CharField(max_length=200, blank=True, null=True, verbose_name='Other',
            help_text='Is there anything else we need to know about your class? \
            Any other comments?')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % (self.name)
