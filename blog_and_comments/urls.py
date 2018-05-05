from django.conf.urls import include, url
from .views import BlogLikeAPIToggle

urlpatterns = [
    url(r'^$', 'blog_and_comments.views.list_blogs', name='list_blogs'),
    url(r'^view_blog/(?P<id>\d+)/$', 'blog_and_comments.views.view_blog', name='view_blog'),
    url(r'^view_blog/like/(?P<id>\d+)/$',  'blog_and_comments.views.blog_like_toggle', name='like_toggle'),
    url(r'^api/view_blog/like/(?P<id>\d+)/$',  BlogLikeAPIToggle.as_view(), name='api_like_toggle'),
    url(r'^create_blog/$', 'blog_and_comments.views.create_blog', name='create_blog'),
    url(r'^update_blog/(?P<id>\d+)/$', 'blog_and_comments.views.update_blog', name='update_blog'),
    url(r'^delete_blog/(?P<id>\d+)/$', 'blog_and_comments.views.delete_blog', name='delete_blog'),
]