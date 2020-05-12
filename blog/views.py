from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(req):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(req, 'blog/post_list.html', {'posts': posts})
    # req에 의해서 html이 전달되어졌다는 것