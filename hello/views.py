from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        'title':'Hello/Index',
        'msg':'これはサンプルで作ったページです。',
        'goto':'next',
    }
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title':'Hello/Next',
        'msg':'これはもう一つのページです。',
        'goto':'index',
    }
    return render(request, 'hello/index.html', params)

def id_name(request, id, nickname):
    result = 'your id: ' + str(id) + ', name: ' + nickname + '.'
    return HttpResponse(result)

def name_age(request, nickname, age):
    result = 'your account: ' + nickname + '(' + str(age) + ').'
    return HttpResponse(result)