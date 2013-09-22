from django import forms
from django.utils.translation import ugettext_lazy as _

from teacher.models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher

    def __init__(self, *args, **kwargs):
        # self.user = kwargs.pop('user', None)
        super(TeacherForm, self).__init__(*args, **kwargs)
