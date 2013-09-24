from django.db import models

NEEDS_CHOICES = (
    ('A', 'Come in and speak to the class about their jobs'),
    ('B','Female programmers to talk about the challenges they face'),
    ('C','Someone to come in and teach a special unit'),
    ('D','Someone to help with an after-school program'),
    ('E','Other'),
)

class Teacher(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=200, blank=False, unique=True,
            verbose_name='Email Address')
    phone = models.CharField(max_length=200)
    school = models.CharField(max_length=200, blank=False,
            verbose_name='At which school do you teach?')
    school_zip_code = models.IntegerField(max_length=5, blank=True, null=True,
            verbose_name="What is the school's zip code? (for pairing purposes")
    grade_age = models.CharField(max_length=10, blank=False,
            verbose_name='What grade/age group do you teach?')
    no_of_students = models.CharField(max_length=4,
            verbose_name='How many students?')
    needs = models.CharField(max_length=1, blank=False, choices=NEEDS_CHOICES,
            verbose_name='Needs', help_text='What kinds of participation from a \
            member of the local programming community would you like to see in \
            your classroom?')
    other = models.CharField(max_length=200, verbose_name='Other',
            help_text='Is there anything else we need to know about your class? \
            Any other comments?')
    created_at = models.DateTimeField(auto_now_add=True)
