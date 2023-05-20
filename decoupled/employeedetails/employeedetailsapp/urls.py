"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
# from productapp import views 
# from . import views 
from .views import EmployeeDetail, Employeeop, Employeeupdate, EmployeeupdateData



urlpatterns = [
    path('employee_details/',EmployeeDetail.as_view(), name="employee"),
    path('employee_details_op/<int:id>/',Employeeop.as_view(), name="employee_op"),
    path('employee_update_op/<int:id>/',Employeeupdate.as_view(), name="employee_update"),
    path('employee_update_data/',EmployeeupdateData.as_view(), name="employee_update"),
    # path('article_detail/<int:id>/',ArticleDetail.as_view(), name="articledetail"),
    # path('task/<int:id>/',Task.as_view(), name="task"),
    # path('generic/article/<int:pk>/',GenericAPIView.as_view(),name="genericapi"),
    # path('secondgeneric/article/<int:pk>/',GenericAPIView.as_view(),name="secondgenericapi"),

]


