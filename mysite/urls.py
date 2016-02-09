from django.conf.urls import url, patterns, include
from django.contrib import admin

urlpatterns = patterns('',
    url(r'$', 'artigos.views.index'),
    url(r'^artigo/(P<url>[^\.]+)', 'artigos.views.artigo'),
    url(r'^admin/', include(admin.site.urls)),
)
