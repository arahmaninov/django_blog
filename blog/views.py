from django.shortcuts import render
from django.http import HttpResponse 
from blog.models import Post
from blog.forms import PostForm

# Create your views here.
# def hello_world(request):
# 	return HttpResponse("<h1> Hello, world! </h1>") 

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'items': posts})

def post_detail(request, post_pk):
	post = Post.objects.get(pk=post_pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	form = PostForm
	return render(request, 'blog/post_new.html', {'form': form})