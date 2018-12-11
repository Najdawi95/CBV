# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from my_app.models import School, Student
from django.core.urlresolvers import reverse_lazy

# Create your views here.

# Function Based View
""" def index(request):
    return render(request, 'index.html') """

# Class Based View
""" class CBV(View):
    def get(self, request):
        return HttpResponse('hello from CBView') """


# Class Based Template View
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['inject_me'] = "injected"
        return context


class SchoolListView(ListView):
    context_object_name = 'schools'
    # to make sure that don't matching the model name / return model_list
    # (the default is school_list - return the lower case model name_details)
    model = School


class SchoolDetailView(DetailView):
    context_object_name = 'school_details'  # return the lower case model name_details
    model = School
    template_name = 'my_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = School


class SchoolDeleteView(DeleteView):
    model = School  # default context name is lower case model name
    success_url = reverse_lazy("my_app:list")  # after delete the field go to school list
