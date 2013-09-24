from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'csta_project.views.home', name='home'),
    url(r'^teachers/', 'teacher.views.teachers', name='teachers'),
    url(r'^developers/', 'developer.views.developers', name='developers'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
