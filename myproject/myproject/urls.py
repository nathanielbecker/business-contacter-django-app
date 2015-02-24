from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView


#### NOTE: for some reason, url patterns need to be entered into THIS urls.py in the myproject folder, and not the other urls.py in cookie_app. Not sure why.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cookie_app/', include('cookie_app.urls')),
    url(r'^$', RedirectView.as_view(url= 'http://quantile-assetman.rhcloud.com/'), name='index'), #
)
