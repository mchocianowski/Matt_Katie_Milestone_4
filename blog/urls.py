from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_posts, name='blog'),
    path('add/', views.add_post, name='add_blog'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
]
