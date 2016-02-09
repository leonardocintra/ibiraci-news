from django.shortcuts import render, get_object_or_404
from artigos.models import Article

def index(request):
	return render(request, 'index.html', {'articles': Article.objects.all() })

def article(request, url):
	return render(request, 'detail.html', {'article': get_object_or_404(Article, url=url)})

