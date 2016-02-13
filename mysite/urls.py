from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from artigos.feeds import ArticleRss

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'artigos.views.index'),
    url(r'^page/(?P<page>[^\.]+)', 'artigos.views.index'),
    url(r'^artigo/(?P<url>[^\.]+)','artigos.views.article'),
    url(r'^form-search/$', 'artigos.views.form_search'),
    url(r'^search/$', 'artigos.views.search'),
    url(r'^contato', 'artigos.views.contact'),
    url(r'^rss/(?P<url>.*)', ArticleRss()),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)
