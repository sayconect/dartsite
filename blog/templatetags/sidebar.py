from django import template
from django.template import context
from blog.views import *
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('blog/popular_tag.html')
def get_popular_posts(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}

@register.inclusion_tag('blog/tegs_list_tag.html')
def show_tegs():
    tegs = Teg.objects.annotate(cnt=Count('posts')).filter(cnt__gt=0)
    return {'tegs': tegs}