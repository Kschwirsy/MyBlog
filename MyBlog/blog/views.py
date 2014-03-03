from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.template import RequestContext
from blog.models import Comment

def index(request):
	#get the blog posts that published
	posts = Post.objects.filter(published=True)
	#now return the rendered template
	return render(request
					, 'blog/index.html'
					, {'posts':posts}
					, context_instance=RequestContext(request))

def about(request):
	return render(request
					, 'blog/about.html'
					, {}
					, context_instance=RequestContext(request))

def post(request, slug):
	#get the Post object
	post = get_object_or_404(Post, slug=slug)
	#now return the rendered template
	return render(request, 'blog/post.html', {'post':post})

