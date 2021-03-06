# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import permalink
from cloudinary.models import CloudinaryField

class Agency(models.Model):
	name = models.CharField('Nome', max_length=50)
	site = models.URLField()

	def __str__ (self):
		return self.name


class Author(models.Model):
	name = models.CharField('Nome', max_length=100)
	email = models.EmailField()

	def __str__ (self):
		return self.name


class Article(models.Model):
	title = models.CharField('Título', max_length=80)
	url = models.SlugField('URL', max_length=200, help_text='URL based in title', unique=True)
	pub_date = models.DateField('Data publicação')	
	content = models.TextField('Conteudo da página')
	authors = models.ManyToManyField(Author)
	agency = models.ForeignKey(Agency)
	imageFeature = CloudinaryField('Imagem', blank=True, null=True)
	imageWidth = models.IntegerField(default=100)
	imageHeight = models.IntegerField(default=100)


	def __str__ (self):
		return self.title

	class Meta:
		ordering = ['-pub_date']
