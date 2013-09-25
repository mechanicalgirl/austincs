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

    if request.method == 'POST':
        form = DeveloperForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context["thankyou"] = Description.objects.get(publish=True, slug='thank-you-for-signing-up')
            return render_to_response("developer_signup_success.html", context,
                    context_instance=RequestContext(request))
        else:
            print form.is_valid()
            print form.errors
    else:
        form = DeveloperForm()

    context["form"] = form

    return render_to_response(template_name, context,
            context_instance=RequestContext(request))
