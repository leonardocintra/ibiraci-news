from django.contrib import admin
from artigos.models import Agency, Author, Article


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')
	search_fields = ('name', 'email')
	ordering = ('name', )


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'agency')
	search_fields = ('title', 'agency')
	list_filter = ('pub_date', )
	date_hierarchy = 'pub_date'
	ordering = ('-pub_date', )
	fields = ('title', 'url', 'pub_date', 'authors', 'agency', 'imageFeature', 'content')
	prepopulated_fields = {'url': ('title', )}
	filter_horizontal = ('authors', )


class AgencyAdmin(admin.ModelAdmin):
	list_display = ('name', 'site', )
	search_fields = ('name', 'site', )
	ordering = ('name', )



admin.site.register(Agency, AgencyAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)