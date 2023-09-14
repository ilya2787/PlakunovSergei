from django.shortcuts import render, redirect
from .models import Post, Likes
from .models import TopicPost
from .models import Photo_post



def Blog(request):
    MyBlog = Post.objects.all()
    topics = TopicPost.objects.all()
    return render(request, 'MyBlog/Blog.html', {"MyBlog": MyBlog, "topics": topics})


def My_topic(request, topic_id):
    MyPost = Post.objects.filter(topic=topic_id)
    Topics = TopicPost.objects.all()
    current_topic = TopicPost.objects.get(id=topic_id)
    context = {'MyPost': MyPost, 'Topics': Topics, 'current_topic': current_topic}
    return render(request, 'MyBlog/my_topic.html', context)


def content_blog(request, content_id):
    blog = Post.objects.get(id=content_id)
    image = Photo_post.objects.filter(post=content_id)
    return render(request, 'MyBlog/content_blog.html', {'blog': blog, 'image': image})

"""Получение ip адресса пользователя"""
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

"""Проверяем ip пользователя и добовляем запись"""
def AddLikes(request, content_id):
    ip_client = get_client_ip(request)
    try:
        Likes.objects.get(ip=ip_client, pos_id=content_id)
        return redirect(f'/Blog/{content_id}')
    except:
        new_like = Likes()
        new_like.ip = ip_client
        new_like.pos_id = int(content_id)
        new_like.save()
        return redirect(f'/Blog/{content_id}')

"""Проверяем ip пользователя и удаляем запись"""
def DisLike(request, content_id):
    ip_client = get_client_ip(request)
    try:
        Lik = Likes.objects.get(ip=ip_client)
        Lik.delete()
        return redirect(f'/Blog/{content_id}')
    except:
        return redirect(f'/Blog/{content_id}')




