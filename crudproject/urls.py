from django.contrib import admin
from django.urls import path
from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
    path('add/', views.AddNew),
    path('update/', views.UpdateRcd),
    path('delete/', views.DeleteRcd),
]
