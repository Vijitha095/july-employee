"""
URL configuration for employeeProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from empApp import views
from app2 import views as app2_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name="home_view"),
    path('reg',views.RegisterView.as_view(),name="register_view"),
    path('delete/<int:id>',views.DeleteView.as_view(),name="delete_view"),
    path('update/<int:id>',views.UpdateView.as_view(),name="update_view"),
    path('emp/reg',app2_views.EmployeeRegisterView.as_view(),name="emp_reg"),
    path('emp/update/<int:empid>',app2_views.EmployeeUpdateView.as_view(),name="emp_update"),
    path('model/reg',app2_views.ModelRegisterView.as_view(),name="model_reg"),
    path('model/update/<int:empid>',app2_views.ModelUpdateView.as_view(),name="model_update"),
]
