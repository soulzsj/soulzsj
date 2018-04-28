from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from grade.models import Grade
from stu.models import Student, StudentInfo, GoodsUser, Goods


def addStu(request):
    if request.method == 'GET':
        return render(request, 'addstu.html')

    if request.method == 'POST':

        stu_name = request.POST.get('name')
        if request.POST.get('sex') == '男':
            stu_sex = 1
        if request.POST.get('sex') == '女':
            stu_sex = 0
        stu_birth = request.POST.get('birth')
        stu_yuwen = request.POST.get('yuwen')
        stu_shuxue = request.POST.get('shuxue')
        Student.objects.create(
            stu_name=stu_name,
            stu_sex=stu_sex,
            stu_birth=stu_birth,
            stu_yuwen=stu_yuwen,
            stu_shuxue=stu_shuxue
        )

        return render(request, 'addstu.html')

def selectStu(request):
    # 查找addr = 相应地址的学生信息
    # stus = StudentInfo.objects.filter(stu_addr='泰国')
    # stu = stus[0]
    # selstu = Student.objects.filter(id=stu.id)
    # stus = StudentInfo.objects.filter(stu_addr__contains='泰国')
    # stu = stus[0]
    # selstu = stu.stu

    # 通过学生表去查找拓展表的信息
    # 查找stu_name为某某的地址
    # 方法1
    # stu = Student.objects.filter(stu_name='宋佳骚').first()
    # selstu = StudentInfo.objects.filter(stu_id=stu.id)

    # 方法2
    stu = Student.objects.filter(stu_name='宋佳骚').first()
    selstu = stu.studentinfo


    return render(request, 'selstu.html', {'selstu':selstu})

def fselStu(request):
    # 查询Python班级下的同学
    # 方法一
    # g = Grade.objects.get(g_name='python')
    # stus = Student.objects.filter(g_id=g.id)
    # 方法二
    # g = Grade.objects.get(g_name='python')
    # stus = g.student_set.all()
    # 查询叫某某同学的班级信息
    # stu = Student.objects.get(stu_name='宋佳雨')
    # gs = stu.g_id
    # 查询python班级下语文成绩大于80分的学生
    # g = Grade.objects.get(g_name='python')
    # stus = g.student_set.filter(stu_yuwen__gte=80)
    # 查询python班级中出生在80后的男生的信息
    # g = Grade.objects.get(g_name='python')
    # stus = g.student_set.filter(stu_birth__gte='1980-01-01', stu_birth__lt='1990-01-01')
    # 查询python班级下语文成绩超过数学成绩10分的男同学信息
    g = Grade.objects.get(g_name='python')
    stus = g.student_set.filter(stu_yuwen__gte=F('stu_shuxue') + 10)

    return render(request, 'selgrade.html', {'stus':stus})


def manyGoods(request):

    # 获取songjiayu购买的商品
    # u = GoodsUser.objects.filter(u_name='宋佳雨')[0]
    # goods = u.goods_set.all()

    # 获取购买娃哈哈的用户的信息
    g = Goods.objects.get(g_name='娃哈哈')
    users = g.g_user.all()

    return render(request, 'goods.html', {'users':users})


def allStudent(request):

    # stus = Student.objects.filter(id=100)
    stus = Student.objects.all()
    return render(request, 'all_stus.html',
                  {'stus': stus}
                  )