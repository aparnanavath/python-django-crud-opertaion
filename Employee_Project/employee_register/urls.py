
from django.urls import path,include
from .import views
 
urlpatterns = [
    path('',views.employee_form,name='employee_insert'), #get and post request for insert operation
    path('list/',views.employee_list,name='employee_list'), #get request to retrievev and dislay all records
    path('<int:id>/',views.employee_form,name='employee_update'), #get and post request fot update operation
    path('delete/<int:id>/',views.employee_delete,name='employee_delete') #get and post request fot update operation
    
]
