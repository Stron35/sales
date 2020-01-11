from django.urls import path
from .views import *

urlpatterns = [
    path('', SalesViewList.as_view(), name='main_page')
]
