# 只会在html端调用，返回刚写的html文件
from django.shortcuts import render


def index(request):
    return render(request, 'multiends/web.html')
