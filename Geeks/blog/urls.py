from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blogPage, name="blogPage"),
    path('blogs/<str:Sno>/', views.blogPost, name='blogPost'),
    path('comments/add/', views.add_comment, name='add_comment'),
    path('comments/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comments/<int:post_id>/', views.list_comments, name='list_comments'),
]

