from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
# This time we are not going to use function but class
# based generic viws by importing it


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
