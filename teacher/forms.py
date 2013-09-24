from django import forms
from django.utils.translation import ugettext_lazy as _

from teacher.models import Teacher, Needs

class TeacherForm(forms.ModelForm):
    needs = forms.ModelMultipleChoiceField(queryset=Needs.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Teacher

    def __init__(self, *args, **kwargs):
        # self.user = kwargs.pop('user', None)
        super(TeacherForm, self).__init__(*args, **kwargs)
