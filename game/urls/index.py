from django.urls import path
from django.urls import include
from game.views.index import index
urlpatterns = [
    # path('game/', include('game.urls')),
    path('', index, name='index'),
    path('menu/', include("game.urls.menu.index")),
    path('playground/', include("game.urls.playground.index")),
    path('settings/', include("game.urls.settings.index")),

]
