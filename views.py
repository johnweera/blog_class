from django.shortcuts import render, HttpResponse
from .models import QuillPost
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy


def index(request):
    return render(request, "blog_class/index.html")


class PostListView(ListView):
    model = QuillPost
    template_name = "blog_class/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = QuillPost
    template_name = "blog_class/post_detail.html"
    context_object_name = "post"


class PostCreateView(CreateView):
    model = QuillPost
    fields = ["title", "content"]
    template_name = "blog_class/post_form.html"
    success_url = reverse_lazy("blog_class:list")


class PostUpdateView(UpdateView):
    model = QuillPost
    fields = ["title", "content"]
    template_name = "blog_class/post_update.html"
    success_url = reverse_lazy("blog_class:list")


class PostDeleteView(DeleteView):
    model = QuillPost
    template_name = "blog_class/post_confirm_delete.html"
    success_url = reverse_lazy("blog_class:list")
    context_object_name = "post"
