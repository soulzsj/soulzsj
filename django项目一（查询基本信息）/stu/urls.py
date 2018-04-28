from django.conf.urls import url

from stu import views

urlpatterns = [
    url(r'addstu/', views.addStu),
    url(r'selstu/', views.selectStu),
    url(r'forstu/', views.fselStu),
    url(r'goods/', views.manyGoods),
    url(r'^stu/', views.allStudent)
]