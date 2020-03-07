"""
Definition of urls for DjangoPolls.
"""

from datetime import datetime
from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views

import app.forms
import app.views

print(r"D:\examples\Python\LearningDjango01\DjangoPolls\DjangoPolls\urls.py started")

print(r"admin.autodiscover()")
admin.autodiscover()

urlpatterns = [
    url(r'^', include('app.urls', namespace="app")),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^seed$', app.views.seed, name='seed'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

print(r"D:\examples\Python\LearningDjango01\DjangoPolls\DjangoPolls\urls.py ended")
