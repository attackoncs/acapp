from django.http.response import HttpResponse


def index(request):
    h1 = "<h1 style='text-align:center'>Hello, world</h1>"
    img = "<img src='https://www.mvprpg.com/upload/article2019-08/20190826102429_365.jpg' style='width:100%'>"
    h1 += img

    return HttpResponse(h1)


def play(request):
    play = '<h1 style="text-align:center">游戏界面</h1>'
    return HttpResponse(play)
