"""
Definition of urls for LearningDjango01.
"""

from django.conf.urls import include, url
import HelloDjangoApp.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^home$', HelloDjangoApp.views.index, name='home'),
]
