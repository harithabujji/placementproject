
from placementapp.views import *
from django.urls import path
from . import views


app_name="placementapp"

urlpatterns=[
        path('stdnts/',get_details),
        path('stdnts/<int:page_number>/', details),
        path('sync/<int:id>/',populate_students),
        ]