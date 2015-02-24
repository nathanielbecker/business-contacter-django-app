# import xadmin###from https://xadmin.readthedocs.org/en/latest/quickstart.html#id2
# xadmin.autodiscover()
# from xadmin.plugins import xversion
# xversion.register_models()

from django.conf.urls import patterns, url, include
# from .views import Initial_Borr_List_PageList, Initial_Borr_List_PageCreate, Initial_Borr_List_PageDetail, Initial_Borr_List_PageUpdate, Initial_Borr_List_PageDelete, tablify
from django.contrib import admin
from cookie_app import views
from django.views.generic.base import RedirectView
# from django.core.urlresolvers import reverse_lazy

#### NOTE: for some reason, url patterns need to be entered into the OTHER urls.py in the myproject folder, and not this urls.py. Not sure why.
urlpatterns = patterns(
    '',
    # url(r'^$', RedirectView.as_view(url= 'google.com'), name='index'), #http://quantile-assetman.rhcloud.com/
    # url(r'^$', RedirectView.as_view(url='http://djangoproject.com'), name='go-to-django'),
    # url(r'^$', Initial_Borr_List_PageList.as_view(), name='Initial_Borr_List_Page_list'),
    # url(r'^new/$', Initial_Borr_List_PageCreate.as_view(), name='Initial_Borr_List_Page_create'),
    # url(r'^(?P<pk>\d+)/$', Initial_Borr_List_PageDetail.as_view(), name='Initial_Borr_List_Page_detail'),
    # url(r'^(?P<pk>\d+)/update/$', Initial_Borr_List_PageUpdate.as_view(), name='Initial_Borr_List_Page_update'),
    # url(r'^(?P<pk>\d+)/delete/$', Initial_Borr_List_PageDelete.as_view(), name='Initial_Borr_List_Page_delete'),
    # url(r'xadmin/',include(xadmin.site.urls)),)
    # (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^myadmin/', include(admin_site.urls)), # this includes the admin text-changing code in admin.py # doesn't work yet
    # url(r'^(?P<pk>\d+)/tablify/$', tablify.as_view(), name='tablify'),
    # url(r'^tablify/?$', 'tablify', name='tablify'),
    # url(r'^tablify/?$', views.tablify, name='tablify'),
)

admin.site.site_header = 'Quantile'
admin.site.site_title = 'Quantile'
admin.site.index_title = 'Quantile'