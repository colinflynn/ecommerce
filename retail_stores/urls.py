from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<retail>.+)/', views.load_store)
]