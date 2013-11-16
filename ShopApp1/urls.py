from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'chris.views.index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'chris.views.post'),
    url(r'^accounts/', include('registration.urls')),
)
