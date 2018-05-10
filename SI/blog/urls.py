from django.conf.urls import url, include
from blog.views import hola
urlpatterns=[
url(r'^$', hola),
]