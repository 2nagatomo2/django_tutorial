from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

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

def id_name(request, id, nickname):
    result = 'your id: ' + str(id) + ', name: ' + nickname + '.'
    return HttpResponse(result)

def name_age(request, nickname, age):
    result = 'your account: ' + nickname + '(' + str(age) + ').'
    return HttpResponse(result)