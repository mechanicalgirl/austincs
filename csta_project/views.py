from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string

from content.models import Description

def home(request):
    """
    """
    template_name = 'home.html'
    context = {}
    context["content"] = Description.objects.get(publish=True, slug='welcome-to-the-austin-csta-project')
    return render_to_response(template_name, context, 
            context_instance=RequestContext(request))

