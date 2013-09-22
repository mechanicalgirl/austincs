from django import forms
from django.utils.translation import ugettext_lazy as _

from developer.models import Developer

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer

    def __init__(self, *args, **kwargs):
        # self.user = kwargs.pop('user', None)
        super(DeveloperForm, self).__init__(*args, **kwargs)
