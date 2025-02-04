from django.shortcuts import render

from django.http import JsonResponse
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    data = [{"title": article.title, "text": article.text, "author": article.author} for article in articles]
    return JsonResponse(data, safe=False)

def article_detail(request, id):
    article = Article.objects.get(id=id)
    data = {"title": article.title, "text": article.text, "author": article.author}
    return JsonResponse(data)
