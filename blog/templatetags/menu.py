from django import template
from blog.models import Category

register = template.Library()

@register.inclusion_tag('blog/menu_tag.html')
def show_menu(class_menu='menu'): # ми додавляємо арг тому що в нас є два одинакових вивода меню в футері і в хедері, і оцей class_menu ми передемов в темплейті в class відкрий menu_tag там буде з самого верху. або якшо далі хз то 7 відео парктичнох частини
    categories = Category.objects.all()
    return  {'categories': categories, 'class_menu': class_menu}