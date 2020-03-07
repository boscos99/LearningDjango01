#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""

import os
import sys

print(r"D:\examples\Python\LearningDjango01\DjangoPolls\manage.py started")

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "DjangoPolls.settings"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

print(r"D:\examples\Python\LearningDjango01\DjangoPolls\manage.py ended")
