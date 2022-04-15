from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list-posts'),
    path('categorias/<int:pk>/', views.PostByCategory.as_view(),
         name='list-posts-by-category'),
]
