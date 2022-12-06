from html.entities import name2codepoint

from django.urls import path

from .views import index, shortner

urlpatterns = [path("", index, name="index"), path("shortner/", shortner, name="shortner")]
