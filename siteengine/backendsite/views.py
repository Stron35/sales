from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.
class SalesViewList(ListView):
    model = Sales
    template_name = 'backendsite/sales.html'
    paginate_by = 10
