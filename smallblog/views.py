from django.shortcuts import render_to_response
from smallblog.models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.order_by('published_time')
    return render_to_response('smallblog/post_list.html',{'posts':posts})


