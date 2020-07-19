from django.urls import path,include
from employee.views import employee_list,employee_details,employee_add,employee_edit,employee_delete


urlpatterns = [
    path('' , employee_list , name="employee_list"),
    path('<int:id>/details' , employee_details , name="employee_details"),
    path('add/' , employee_add , name="employee_add"),
    path('<int:id>/edit' , employee_edit , name="employee_edit"),
    path('<int:id>/delete' , employee_delete , name="employee_delete")

]