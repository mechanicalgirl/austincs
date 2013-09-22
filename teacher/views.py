from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string

from teacher.models import Teacher
from content.models import Description
from teacher.forms import TeacherForm

def teachers(request):
    """
    """
    template_name = 'teacher_signup.html'

    context = {}
    context["content"] = Description.objects.get(publish=True, slug='central-texas-cs-teachers')
    context["form"] = TeacherForm()

    return render_to_response(template_name, context,
            context_instance=RequestContext(request))
