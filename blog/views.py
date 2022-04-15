from django.views import generic
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/blog.html"


class PostByCategory(generic.ListView):
    model = Post
    template_name = "blog/categorias.html"

    def get_queryset(self):
        return Post.objects.filter(categorias__id=self.kwargs['pk'])
