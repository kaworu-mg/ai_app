from django.urls import path
from . import views

urlpatterns = {
  path("", views.index, name="home")#viewsからindexを取り出す
}