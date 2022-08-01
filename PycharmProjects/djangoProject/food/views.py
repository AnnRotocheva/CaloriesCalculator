from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Product


def get(request):
    ml = Product.objects.all()
    ctx = {'list': ml}
    return render(request, 'food/list.html', ctx)

def detail(request, name_id):
    try:
        a = Product.objects.get(id = name_id)
        b = {'product': a}
    except:
        raise Http404('Тут пусто :с')
    return render(request, 'food/detail.html', b)