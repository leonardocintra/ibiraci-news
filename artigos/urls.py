from django.conf.urls import url
from django.contrib import admin
from artigos.feeds import ArticleRss
from . import views

admin.autodiscover()

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^page/(?P<page>[^\.]+)', 'artigos.views.index'),
    url(r'^artigo/(?P<url>[^\.]+)','artigos.views.article'),
    url(r'^form-search/$', 'artigos.views.form_search'),
    url(r'^pesquisa/$', 'artigos.views.search'),
    url(r'^contato', 'artigos.views.contact'),
    url(r'^rss/(?P<url>.*)', ArticleRss()),
]