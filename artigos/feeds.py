from django.contrib.syndication.views import Feed
from models import Article

class ArticleRss(Feed):
	title = "Ultimos artigos do site"
	link = "/"
	description = "Ultimas noticias publicadas"

	def items(self):
		return Article.objects.all()

	def item_link(self, article):
		return "/artigo/%s" % article.url

	def item_description(self, article):
		return article.content