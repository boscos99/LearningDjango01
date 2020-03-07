"""
Customizations for the Django administration interface.
"""

from django.contrib import admin
from app.models import Choice, Poll

print(r"D:\examples\Python\LearningDjango01\DjangoPolls\app\admin.py started")

class ChoiceInline(admin.TabularInline):
    """Choice objects can be edited inline in the Poll editor."""
    print(r"Choice objects can be edited inline in the Poll editor.")
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    """Definition of the Poll editor."""
    print(r"Definition of the Poll editor.")
    fieldsets = [
        (None, {'fields': ['text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['text']
    date_hierarchy = 'pub_date'


print(r"admin.site.register(Poll, PollAdmin)")
admin.site.register(Poll, PollAdmin)

print(r"D:\examples\Python\LearningDjango01\DjangoPolls\app\admin.py ended")

