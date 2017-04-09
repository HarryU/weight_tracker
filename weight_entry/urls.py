from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.weight_graph, name='weight_graph'),
]
