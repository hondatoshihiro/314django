#from django.urls import re_path
from django.urls import path
from . import views
#この記載はなに(カレントディレクトリから、viewsを読み込むってこと)

urlpatterns = [
#    re_path(r'', RecordLaptimeView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
]