from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string

from teacher.models import Teacher, Needs
from content.models import Description
from teacher.forms import TeacherForm

def teachers(request):
    """
    """
    template_name = 'teacher_signup.html'

    context = {}
    context["content"] = Description.objects.get(publish=True, slug='central-texas-cs-teachers')

    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context["thankyou"] = Description.objects.get(publish=True, slug='thank-you-for-signing-up')
            return render_to_response("teacher_signup_success.html", context,
                    context_instance=RequestContext(request))
        else:
            print form.is_valid()
            print form.errors
    else:
        form = TeacherForm() #No post data

    context["form"] = form

    return render_to_response(template_name, context,
            context_instance=RequestContext(request))
