from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings

from artigos.models import Article
from artigos.forms import FormContact


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
	page_url = "artigo/" + url
	imagem_url = "/media/" + settings.MEDIA_URL
	return render(request, 'detail.html', {
		'article': get_object_or_404(Article, url=url), 
		'page_url': page_url,
		'media_url': imagem_url
	})


def form_search(request):
	return render(request, 'search_form.html')


def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		articles = Article.objects.filter(title__contains=q) | Article.objects.filter(content__contains=q)
		return render(request, 'search_results.html', {'articles': articles, 'query': q})
	else:
		return render(request, 'search_form.html', {'error': True })


def contact(request):
	page_url = 'contato'

	if request.method == "POST":
		form = FormContact(request.POST)
		if form.is_valid():
			recipient = ['emaildevleonardo@gmail.com']
			sender = form.cleaned_data['email']
			subject = "CONTATO - " + form.cleaned_data['name']
			message = "TELEFONE: " + form.cleaned_data['phone'] + "\n MENSAGEM:" + form.cleaned_data['message'] + "\n EMAIL: " + form.cleaned_data['email']
			print("Enviado email para: " + sender)
			send_mail(subject, message, sender, recipient)

			return render(request, 'contact.html', {'form': FormContact(), 'send':True, 'page_url': page_url })
	else:
		form = FormContact()

	return render(request, 'contact.html', {'form': form, 'page_url': page_url })



