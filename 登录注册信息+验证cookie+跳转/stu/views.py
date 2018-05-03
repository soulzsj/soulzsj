from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

# Create your views here.
from stu.models import Student, StudentInfo
from uauth.models import Users


def index(request):

    if request.method == 'GET':
        # 获取学生信息
        # ticket = request.COOKIES.get('ticket')
        # if not ticket:
        #     return HttpResponseRedirect('/uauth/login/')
        # if Users.objects.filter(u_ticket=ticket).exists():
        #     stuinfos = StudentInfo.objects.all()
        #     return render(request, 'index.html', {'stuinfos':stuinfos})
        # else:
        #     return HttpResponseRedirect('/uauth/login/')
        stuinfos = StudentInfo.objects.all()
        return render(request, 'index.html', {'stuinfos':stuinfos})


def addStu(request):
    if request.method == 'GET':

        return render(request, 'addstu.html')

    if request.method == 'POST':
        # 跳转到学生详情方法中
        name = request.POST.get('name')
        tel = request.POST.get('tel')


        stu = Student.objects.create(
            s_name=name,
            s_tel=tel
        )

        return HttpResponseRedirect(
            reverse('s:addinfo', kwargs={'stu_id':stu.id})
        )


def addStuinfo(request, stu_id):

    if request.method == 'GET':

        return render(request, 'addstuinfo.html', {'stu_id':stu_id})
    if request.method == 'POST':
        stu_id = request.POST.get('stu_id')
        age = request.POST.get('age')
        addr = request.POST.get('addr')
        # 添加图片
        img = request.FILES.get('img')


        StudentInfo.objects.create(s_addr = addr, s_age=age, s_id=stu_id, s_image=img)

        return HttpResponseRedirect('/stu/index/')
#     return HttpResponseRedirect(reverse(
#         's:alls', kwargs={'s_id':s_id}
#     )), render(request, 'addstuinfo.html')
#
# def showAllstu(request):
#
#     stus = Student.objects.all()
#     stuss = StudentInfo.objects.all()
#
#     return render(request, 'allstu.html', {'stus':stus}, {'stuss':stuss})

def stuPage(request):

    if request.method == 'GET':

        page_id = request.GET.get('page_id', 1)
        stus = Student.objects.all()
        paginator = Paginator(stus, 3)
        page = paginator.page(int(page_id))
        return render(request, 'index_page.html', {'stus':page})

