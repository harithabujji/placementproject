import MySQLdb
import click
import os,django
import requests
from django.views.generic import UpdateView

from placementapp.models import *

from django.shortcuts import *
from django.views.generic import *

from placementproject import settings

from django.urls import *

app_name="placementapp"


#creates environment variable for running django commands through script.
def setup_django():
    os.environ["DJANGO_SETTINGS_MODULE"] = 'placementproject.settings'
    django.setup()


#Populates students table.
def populate_students(id):
    # importing Student
    from placementapp.models import Student

    url = r"http://www.bhageerathreddy.com/mrnd-hackathon/2018/api/students/"
    data = requests.get(url)
    msg=data.json()['message']

    for i in msg:
        print(i)
        # if i['id']==id:
        #     print(id)
        #     s = Student(name=i['name'])
        #     s.save()
        #     break


