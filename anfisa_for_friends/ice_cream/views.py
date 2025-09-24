from django.shortcuts import render, get_object_or_404

from ice_cream.models import IceCream

def ice_cream_detail(request, pk):

    return render(
        request,
        template_name='ice_cream/detail.html',
        context={
            # Вызываем .get() и в его параметрах указываем условия фильтрации:
            'ice_cream': get_object_or_404(
                IceCream.objects.filter(
                    is_published=True, category__is_published=True
                ),
                pk=pk
                ),
            }
    )


def ice_cream_list(request):

    return render(
        request,
        template_name='ice_cream/list.html',
        context={
            'ice_cream_list': IceCream.objects.select_related('category')
            .filter(is_published=True, category__is_published=True)
            .order_by('category')
            }
        )
