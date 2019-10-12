from django.urls import path

from . import views

app_name = "tools"

urlpatterns = [
path("", views.StartPage.as_view(), name="startpage"),
path("my_tools/", views.MyToolsView.as_view(), name="mytools"),
path("new_tool/", views.NewToolView.as_view(), name="newtool"),
path("delete/<str:pk>", views.DeleteToolView.as_view(), name="deletetool"),
path("neighbors/",views.NeighborsView.as_view(), name="neighbors"),
path("borrower_feed/", views.BorrowerView.as_view(), name="borrower_feed")
]
