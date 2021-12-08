from django import template
from django.http.response import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import F

# Create your views here.

class HomeList(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'news'
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.all()



class NewsByCategory(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'news'
    paginate_by =  8
    allow_empty = False # при звертанні до пустої категорії або категорії якої не існує вибиває 404

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titl'] = 'fdsfd'
        return context

    def get_queryset(self):
        # тако не треба бо ми не виводим категорію там і тег, але лишу для наглядності
        # return Post.objects.filter(category__slug=self.kwargs['category_slug']).select_related('category').prefetch_related('tags')
        return Post.objects.filter(category__slug=self.kwargs['category_slug'])



class NewsBySlug(DetailView):
    model = Post
    template_name = 'blog/news.html'
    context_object_name = 'news'

    def get_object(self):
        try:
            return Post.objects.get(slug=self.kwargs['slug'])
        except:
            raise Http404("Post doesn't exist")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1 # Так ми пишем щоб робити 1+ до перегляду коли ми заходимо на сайт
        self.object.save() # якщо написати тільки оце тоді  воно збереже просто вираз
        self.object.refresh_from_db() # а так воно ніби обновить все і бцде показувати число
        return  context 



class NewsByTag(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'news'
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

# 16 відео там видно як то всьо робити. Головне з пагінацією не провтикати там в  html треба один двіж зробити!!! а якщо будти точним то вказати оце ?{{  search  }}page={{  p  }} . search після ? щоб при переході на некст ст не втрачався пошук
class SearchPosts(ListView):
    model = Post
    template_name = 'blog/post_search.html'
    context_object_name = 'news'
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('search'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = f"search={self.request.GET.get('search')}&" # це ми робмо для тогог щоб у випадку якщо результат займає дві сторірки при переході на наступну параметре search не пропадав
        context['search_by'] = self.request.GET.get('search')
        return context
