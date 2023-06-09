from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.page, name="page"),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("rpage/", views.rpage, name="rpage"),
    path("test", views.test, name="test")
]
