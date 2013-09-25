import datetime

from django.conf import settings
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string

from contact.forms import ContactForm

def contactus(request):
    template_name = 'contact.html'

    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
	    sender = form.cleaned_data['email']
            sender_name = form.cleaned_data['name']
	    message = form.cleaned_data['message']
            from django.core.mail import send_mail
            email_dict = { 'sender': sender, 'sender_name': sender_name, 'message': message, 'date': datetime.date.today() }
            subject = "Contact message sent from austincs.org"
            body = render_to_string('contact_notification.txt', email_dict)
            sent = send_mail(subject, body, settings.ADMINS[0][1], [settings.ADMINS[0][1]])
	    context['message'] = message
    else:
        form = ContactForm()

    context['form'] = form

    return render_to_response(template_name, context,
            context_instance=RequestContext(request))
