from django.conf.urls import url

from stu import views

urlpatterns = [
    url(r'index/', views.index),
    url(r'addstu/', views.addStu, name='add'),
    url(r'addstuinfo/(?P<stu_id>\d+)/', views.addStuinfo, name='addinfo'),
    url(r'stupage/', views.stuPage),
    # url(r'showallstu/(\d+)/', views.showAllstu, name='alls')
]