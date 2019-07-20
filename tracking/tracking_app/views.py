import os

from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView

class DashboardView(TemplateView):
    template_name=os.path.join('tracking_app', 'dashboard.html')

