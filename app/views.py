from django.shortcuts import render
from django.views.generic import ListView,FormView,DetailView,CreateView,UpdateView
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
class school_list(ListView):
    model = School
    context_object_name = 'schools'
    ordering = ['sname']
class displayschool(DetailView):
    model = School
    context_object_name = 'schoolobj'


class school_insert(CreateView):
    model= School
    fields = '__all__'
    success_url = 'school_list'

class school_update(UpdateView):
   model = School
   fields = '__all__'
   success_url = 'school_list'