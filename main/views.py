from django.shortcuts import render
from django.http import HttpResponse
from .models import Random_number


def index(request):
    random_numbers = Random_number.objects.all()
    joining = ', '.join([str(i.num) for i in random_numbers])
    context = {'joining': joining}
    return render(request, 'main/index.html', context)


def detail(request,foo1):
    return HttpResponse('{}'.format(foo1))


def results(request):
    return HttpResponse('results')


def vote(request):
    return HttpResponse('vote')
