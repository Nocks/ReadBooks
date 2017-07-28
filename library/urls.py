from django.conf.urls import url
from library import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
