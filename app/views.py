from django.shortcuts import render
from django.views.generic import ListView,FormView
from .models import *
from app.forms import SchoolForm
from django.http import HttpResponse
# Create your views here.


class school_form_cbv(FormView,ListView):
    template_name = 'school_list_cbv.html'
    form_class = SchoolForm
    model = School
    context_object_name = 'schools'

    def form_valid(self, form):
        form.save()
        return HttpResponse("data added by formview")
    
    


class school_list_cbv(ListView):
    model = School
    context_object_name = 'schools'
    template_name = 'school_list_cbv.html'
    ordering = ['sname']