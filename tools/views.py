from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Tool
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model

User = get_user_model()


class StartPage(generic.TemplateView):
    template_name = "tools/start_page.html"


class MyToolsView(LoginRequiredMixin, generic.ListView):
    template_name = "tools/my_tools.html"
    model = Tool
    context_object_name = "tool_list"
    def get_queryset(self):
        return Tool.objects.filter(owner=self.request.user)


class NewToolView(LoginRequiredMixin, generic.CreateView):
    model = Tool
    fields = ["name","type","is_available",]
    template_name = "tools/new_tool.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy("tools:mytools")


class DeleteToolView(LoginRequiredMixin, generic.DeleteView):
    model = Tool

    def get_object(self, queryset=None):
        tool = super(DeleteToolView, self).get_object()
        if not tool.owner == self.request.user:
            raise Http404
        return tool
    success_url = reverse_lazy("tools:mytools")


class NeighborsView(generic.ListView):
    model = User
    template_name = "tools/neighbors.html"
    context_object_name = "neighbors_list"
    def get_queryset(self):
        return User.objects.exclude(username="admin")

class BorrowerView(LoginRequiredMixin,generic.ListView):
    model = Tool
    template_name = "tools/borrower.html"
    context_object_name = "borrower_list"

    def get_queryset(self):
        return Tool.objects.all()
