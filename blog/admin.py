from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'



class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} # слаг буде будуватися на основі вказаних полів( а наам треба на основі тайтла)
    form = PostAdminForm
    list_display = ('id','title','slug', 'author', 'created_at', 'views', 'category', 'is_there_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ['category']
    readonly_fields = ('views','created_at', 'is_there_photo')
    fields = ('title','slug', 'author','content', 'created_at', 'views', 'category','tags', 'photo', 'is_there_photo')

    save_as = True # нааприклад треба створити 10 постів де буде відрізнятися лише одне поле, тоді при цьому параметрі ти прост міняєш необхідне поле і воно зберігається як новий обєект
    save_on_top = True

    def is_there_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:  
            return'no'
    is_there_photo.short_description = 'Photo'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')


admin.site.register(Teg, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

