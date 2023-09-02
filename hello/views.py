from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import HelloForm
from .forms import FriendForm
from .forms import CreateForm
from .forms import FindForm
from .models import Friend
from django.db.models import QuerySet
from django.db.models import Q

class HelloView(TemplateView):
    def __init__(self) -> None:
        self.params = {
            'title':'Hello',
            'message':'your data:',
            'form':HelloForm(),
            'result':None,
            'checks':None,
            'choice':None,
            'radio':None,
        }
    
    def get(self, request):
        return render(request, 'hello/index.html', self.params)
    
    def post(self, request):
        msg = 'あなたは、<b>' + request.POST['name'] + '(' + request.POST['age'] + ')<b>さんです。<br>メールアドレスは<b>' + request.POST['mail'] + '<b>ですね。'
        self.params['message'] = msg
        if 'check' in request.POST:
            self.params['result'] = 'Checked!'
        else:
            self.params['result'] = 'not checked...'
        chk = request.POST['checks']
        self.params['checks'] = 'you selected: ' + chk
        ch = request.POST['choice']
        self.params['choice'] = 'selected: ' + ch
        rad = request.POST['choices']
        self.params['radio'] = 'selected: ' + rad
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)

def friend(request):
    params = {
        'title': 'Friend',
        'message': 'all friends',
        'form': FriendForm(),
        'data': [],
    }
    if(request.method == 'POST'):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = FriendForm(request.POST)
    else:
        params['data'] = Friend.objects.all()
    return render(request, 'hello/friend.html', params)

def __new__str__(self):
    result = ''
    for item in self:
        result += '<tr>'
        for k in item:
            result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
        result += '</tr>'
    return result

QuerySet.__str__ = __new__str__

def friend_record(request):
    data = Friend.objects.all()
    params = {
        'title': 'friend record',
        'data': data,
    }
    return render(request, 'hello/friend_record.html', params)

#create model
def create(request):
    if(request.method == 'POST'):
        obj = Friend()
        friend = CreateForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello/friend/record')
    params = {
        'title': 'Create',
        'form': CreateForm(),
    }
    return render(request, 'hello/create.html', params)

#edit model
def edit(request, num):
    obj = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend = CreateForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello/friend/record')
    params = {
        'title': 'edit',
        'id': num,
        'form': CreateForm(),
    }
    return render(request, 'hello/edit.html', params)

#delete model
def delete(request, num):
    friend = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello/friend/record')
    params = {
        'title': 'delete',
        'id': num,
        'obj': friend
    }
    return render(request, 'hello/delete.html', params)

def find(request):
    if request.method == 'POST':
        msg = 'search result'
        form = FindForm(request.POST)
        str = request.POST['find']
        data = Friend.objects.filter(Q(name__icontains=str) | Q(mail__icontains=str))
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'find',
        'msg': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'hello/find.html', params)



def id_name(request, id, nickname):
    result = 'your id: ' + str(id) + ', name: ' + nickname + '.'
    return HttpResponse(result)

def name_age(request, nickname, age):
    result = 'your account: ' + nickname + '(' + str(age) + ').'
    return HttpResponse(result)