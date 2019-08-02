import os

from django.shortcuts import render
from django.views.generic import (TemplateView, 
                                  CreateView, 
                                  ListView, 
                                  DetailView,
                                  UpdateView)
from tracking_app.models import *
from common.utilities import ContextMixin
from tracking_app import forms


class DashboardView(TemplateView):
    template_name=os.path.join('tracking_app', 'dashboard.html')


class BusinessHomePage(ContextMixin, TemplateView):
    template_name=os.path.join('tracking_app', 'business','home.html')
    extra_context = {
        'customers': Customer.objects.all()
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user.username
        #TODO find business name
        return context


class CustomerCreateView(ContextMixin, CreateView):
    template_name = os.path.join('common', 'create_template.html')
    model = Customer
    form_class = forms.CustomerForm
    extra_context = {
        'title': 'Create Customer'
    }
    #TODO create user whenever a customer is created


class CustomerSubaccountListView(ListView):
    template_name=os.path.join('tracking_app', 'customer', 'account_list.html')
    
    def get_queryset(self):
        customer = Customer.objects.get(pk=self.kwargs['pk'])
        return Customer.objects.filter(parent_customer=customer)

class CustomerUpdateView(ContextMixin, UpdateView):
    template_name = os.path.join('common', 'create_template.html')
    model = Customer
    form_class = forms.CustomerUpdateForm
    extra_context = {
        'title': 'Update Customer'
    }

class CustomerDetailView(DetailView):
    template_name = os.path.join('tracking_app', 'customer', 'detail.html')
    model = Customer

class SubAccountListView(ListView):
    pass


class DeviceListView(ListView):
    template_name = os.path.join('tracking_app', 'devices', 'list.html')
    model = Device


class DeviceCreateView(ContextMixin, CreateView):
    form_class = forms.DeviceCreateForm
    template_name = os.path.join('common', 'create_template.html')
    extra_context = {
        'title': 'Add Device'
    }

class DeviceUpdateView(ContextMixin, UpdateView):
    model = Device
    form_class = forms.DeviceUpdateForm
    template_name = os.path.join('common', 'create_template.html')
    extra_context = {
        'title': 'Update Device Details'
    }


class MonitorHome(ContextMixin, TemplateView):
    template_name = os.path.join('tracking_app', 'monitor','home.html')
    extra_context = {
        'devices_list': [{
            'name': 'Test Device',
            'status': 'offline'
        }]
    }

class StatisticsView(ContextMixin, TemplateView):
    template_name = os.path.join('tracking_app', 'monitor', 'statistics.html')
    extra_context = {
       'form': forms.ReportForm()
    }
class DevicesListView(ListView):
    model = Device
    template_name = os.path.join('tracking_app', 'devices', 'full_list.html')

    
class MovingOverViewReport(TemplateView):
    template_name = os.path.join('tracking_app', 'reports', 
        'moving_overview.html')
    