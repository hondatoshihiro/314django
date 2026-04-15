from django.urls import path
#この記載はなに(カレントディレクトリから、viewsを読み込むってこと)
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
]