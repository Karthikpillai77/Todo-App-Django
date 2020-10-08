from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('delete/<int:id>/',views.delete_view),
]
