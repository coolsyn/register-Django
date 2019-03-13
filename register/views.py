from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from register.models import Participator


# Create your views here.
#自定义表单模型
class ParticipatorForm(forms.Form):
    Sname = forms.CharField(label = '姓名:',max_length = 10)
    Sid = forms.CharField(label = '学号:',max_length=20)
    Email = forms.EmailField(label = '邮箱:')
    Sex = forms.CharField(label='性别:',max_length=4)
    Department = forms.CharField(label='院系:',max_length=100)
    Major_class = forms.CharField(label='专业班级:',max_length=100)
    Phone_number = forms.CharField(label='手机号码:',max_length=20)
    Declaration = forms.CharField(label='参赛宣言:',max_length=200)
    Resume = forms.CharField(label='个人简介:',max_length=100)
    Comprehension = forms.CharField(label='主题理解:',max_length=100)

def register(request):
    if request.method == 'POST':
        pf = ParticipatorForm(request.POST)
        if pf.is_valid():
            #获取表单元素
            Sname = pf.cleaned_data['Sname']
            Sid = pf.cleaned_data['Sid']
            Email = pf.cleaned_data['Email']
            Sex = pf.cleaned_data['Sex']
            Phone_number = pf.cleaned_data['Phone_number']
            Department = pf.cleaned_data['Department']
            Declaration = pf.cleaned_data['Declaration']
            Major_class = pf.cleaned_data['Major_class']
            Resume = pf.cleaned_data['Resume']
            Comprehension = pf.cleaned_data['Comprehension']

            #将表单写入数据库
            user = Participator()
            user.Sname = Sname
            user.Sid = Sid
            user.Email = Email
            user.Declaration = Declaration
            user.Phone_number = Phone_number
            user.Sex = Sex
            user.Comprehension = Comprehension
            user.Major_class = Major_class
            user.Resume = Resume
            user.Department = Department
            user.save()
            #返回注册成功页面
            return render_to_response('success.html',{'Sname':Sname})
    else:
        pf = ParticipatorForm()
    return render_to_response('register.html',{'pf':pf})
