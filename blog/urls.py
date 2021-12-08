from .views import *
from django.urls import path


urlpatterns = [
    path('', HomeList.as_view(), name='home'),
    path('category/<slug:category_slug>/', NewsByCategory.as_view(), name='category'),
    path('news/<slug:slug>/', NewsBySlug.as_view(), name='news'),
    path('tag/<str:slug>/', NewsByTag.as_view(), name='tag'),
    path('search/', SearchPosts.as_view(), name='search'),
    ]

