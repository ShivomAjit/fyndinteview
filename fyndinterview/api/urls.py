from django.conf.urls import url
from .views import *

app_name = 'api'

urlpatterns = [
    url(r'^details', IndexApiView.as_view(), name='index'),
]
