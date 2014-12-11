from django.conf.urls import patterns, url, include
from .views import barebones_CRUDList, barebones_CRUDCreate, barebones_CRUDDetail, barebones_CRUDUpdate, barebones_CRUDDelete, tablify
from django.contrib import admin
from cookie_app import views
# from cookie_app.admin import admin_site # doesn't work yet

urlpatterns = patterns(
    '',
    url(r'^$', barebones_CRUDList.as_view(), name='barebones_crud_list'),
    url(r'^new/$', barebones_CRUDCreate.as_view(), name='barebones_crud_create'),
    url(r'^(?P<pk>\d+)/$', barebones_CRUDDetail.as_view(), name='barebones_crud_detail'),
    url(r'^(?P<pk>\d+)/update/$', barebones_CRUDUpdate.as_view(), name='barebones_crud_update'),
    url(r'^(?P<pk>\d+)/delete/$', barebones_CRUDDelete.as_view(), name='barebones_crud_delete'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^myadmin/', include(admin_site.urls)), # this includes the admin text-changing code in admin.py # doesn't work yet
    # url(r'^(?P<pk>\d+)/tablify/$', tablify.as_view(), name='tablify'),
    # url(r'^tablify/?$', 'tablify', name='tablify'),
    url(r'^tablify/?$', views.tablify, name='tablify'),

)

admin.site.site_header = 'Nerva Data Systems'
admin.site.site_title = 'Hello User'
admin.site.index_title = 'Doop'