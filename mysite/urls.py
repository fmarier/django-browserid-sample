from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^$', 'mysite.views.home'),
    (r'^browserid/', include('django_browserid.urls')),
)

urlpatterns += staticfiles_urlpatterns()
