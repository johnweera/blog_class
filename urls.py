from django.urls import path
from . import views

app_name = "blog_class"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.PostCreateView.as_view(), name="add"),
    path("list/", views.PostListView.as_view(), name="list"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.PostUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
]
