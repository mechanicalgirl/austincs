from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string

from developer.models import Developer
from content.models import Description
from developer.forms import DeveloperForm

def developers(request):
    """
    """
    template_name = 'developer_signup.html'

    context = {}
    context["content"] = Description.objects.get(publish=True, slug='developers-austin-csta-volunteer-program-sign-ups')
    context["form"] = DeveloperForm()

    return render_to_response(template_name, context,
            context_instance=RequestContext(request))
