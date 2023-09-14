from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('travel', views.travel, name="travel"),
    path('about_me', views.about_me, name="about_me"),
    path('meditation', views.meditation, name="meditation"),
    path('seo', views.seo, name="seo"),
    path('massag', views.massag, name="massag"),
]
