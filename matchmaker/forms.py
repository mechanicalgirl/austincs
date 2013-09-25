from django import forms

from matchmaker.models import Match

class MatchForm(forms.ModelForm):

    class Meta:
        model = Match

    def __init__(self, *args, **kwargs):
        # self.user = kwargs.pop('user', None)
        super(MatchForm, self).__init__(*args, **kwargs)
