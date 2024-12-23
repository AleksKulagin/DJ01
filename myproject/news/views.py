from django.shortcuts import render
from .models import News_post

def home(request):
	news = News_post.objects.all()
	return render(request, 'news/new1.html', {'news': news})