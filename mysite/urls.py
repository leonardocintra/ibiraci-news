from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'artigos.views.index'),
    url(r'^paginacao/(?P<page>[^\.]+)', 'artigos.views.index'),
    url(r'^artigo/(?P<url>[^\.]+)','artigos.views.article'),
    url(r'^form-search/$', 'artigos.views.form_search'),
    url(r'^search/$', 'artigos.views.search'),
    url(r'^contact', 'artigos.views.contact'),
    url(r'^admin/', include(admin.site.urls)),
)
