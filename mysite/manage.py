#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
 
    #Check if webscraping txt file exist in folder, if:
    #   in static folder, skip webscraping
    #   if not in static folder, do webscraping
    #   this should only happen once per seemster 

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
