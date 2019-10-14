from django.urls import path

from . import views

app_name = "tools"

urlpatterns = [
path("", views.StartPage.as_view(), name="base"),
path("my_tools/", views.MyToolsView.as_view(), name="mytools"),
path("new_tool/", views.NewToolView.as_view(), name="newtool"),
path("delete/<int:pk>", views.DeleteToolView.as_view(), name="deletetool"),
path("update_tool/<int:pk>", views.UpdateToolView.as_view(), name="update_tool"),
path("neighbors/",views.NeighborsView.as_view(), name="neighbors"),
path("borrower_feed/", views.BorrowerView.as_view(), name="borrower_feed"),
path("users_tool/<int:pk>", views.UsersToolView.as_view(), name="users_tool")
]
