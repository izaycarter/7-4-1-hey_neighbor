from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Tool
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from django.views import generic


class StartPage(generic.TemplateView):
    template_name = "tools/start_page.html"


class MyToolsView(LoginRequiredMixin, generic.ListView):
    template_name = "tools/my_tools.html"
    model = Tool


class NewToolView(LoginRequiredMixin, generic.CreateView):
    model = Tool
    # fields = '__all__'
    fields = ["name","is_available"]
    template_name = "tools/new_tool.html"
