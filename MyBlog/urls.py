from django.urls import path
from . import views

urlpatterns = [
    path('topic_<int:topic_id>/', views.My_topic, name="My_topic"),
    path('<int:content_id>/', views.content_blog, name="content_blog"),
    path('<int:content_id>/add_likes', views.AddLikes, name="Add_Like"),
    path('<int:content_id>/del_likes', views.DisLike, name="Dis_Like"),
    path('', views.Blog, name="Blog"),
]
