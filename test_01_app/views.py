from django.shortcuts import render

# Create your views here.
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'test_01_app/post_list.html', {'posts': posts})
