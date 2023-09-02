from django import forms
from .models import Friend

class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.EmailField(label='mail')
    age = forms.IntegerField(label='age')

    #チェックボックス(2択)
    check = forms.BooleanField(label='Checkbox', required=False)

    #３択
    checks = forms.NullBooleanField(label='Checks')

    data = [
        ('one', 'item 1'),
        ('two', 'item 2'),
        ('three', 'item 3')
    ]
    #プルダウン
    choice = forms.ChoiceField(label='choice', choices=data)

    data_radio = [
        ('one', 'radio 1'),
        ('two', 'radio 2'),
        ('three', 'radio 3')
    ]
    #ラジオボタン
    choices = forms.ChoiceField(label='radio', choices=data_radio, widget=forms.RadioSelect())

class FriendForm(forms.Form):
    id = forms.IntegerField(label='ID')

class CreateForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)