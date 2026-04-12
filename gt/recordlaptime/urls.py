from django.urls import path
#この記載はなに(カレントディレクトリから、viewsを読み込むってこと)
from . import views

urlpatterns = [
    path('<int:id>/<nickname>/', views.index, name='index'),
]