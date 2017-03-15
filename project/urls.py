from django.conf.urls import patterns, include, url
from django.contrib import admin
from calc import views

urlpatterns = patterns('',
    url(r'(\d+)([\+\-\*/])(\d+)', views.calcula, name="calcula"),
    url(r'(.*)', views.notfound, name="notfound"),
)
