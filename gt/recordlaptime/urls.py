from django.urls import re_path
from .views import RecordLaptimeView
#この記載はなに(カレントディレクトリから、viewsを読み込むってこと)

urlpatterns = [
    re_path(r'', RecordLaptimeView.as_view(), name='index'),
]