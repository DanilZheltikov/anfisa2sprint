from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream, Category

def index(request):
    
    return render(
        request,
        template_name='homepage/index.html',
        context={
            # Полученный из БД QuerySet передаём в словарь контекста:
            'ice_cream_list': IceCream.objects.values(
                'title', 'id', 'description', 'price'
            ).filter(
                is_published=True, is_on_main=True, category__is_published=True
                )
        }
    )
