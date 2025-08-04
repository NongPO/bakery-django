#!/usr/bin/env python
"""
สคริปต์สำหรับรวบรวม static files สำหรับ production
ใช้รันคำสั่ง: python collect_static.py
"""
import os
import sys
import django
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bakery_django.settings')
    django.setup()
    
    # Run collectstatic command
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
