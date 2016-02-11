from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from artigos.models import Article

def index(request, page=1):
	pagination = Paginator(Article.objects.all(), 3)
	try:
		summary = pagination.page(page)
	except PageNotAnInteger:
		summary = pagination.page(1)
	except EmptyPage:
		summary = pagination.page(pagination.num_pages)

	return render(request, 'index.html', {
		'articles': summary.object_list,
		'pagination': summary,
		'page_now': page, })

def article(request, url):
	return render(request, 'detail.html', 
		{'article': get_object_or_404(Article, url=url)})

def form_search(request):
	return render(request, 'search_form.html')

def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		articles = Article.objects.filter(title__contains=q) | Article.objects.filter(content__contains=q)
		return render(request, 'search_results.html', {'articles': articles, 'query': q})
	else:
		return render(request, 'search_form.html', {'error': True })


