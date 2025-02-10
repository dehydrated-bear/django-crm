from django.urls import path

from .views import lead_list,lead_view,lead_create,lead_update,lead_delete,landing_page

app_name="leads"

urlpatterns=[
    path('',lead_list,name="lead_list"),
    path('<int:pk>/',lead_view,name="lead_view"),
    path('<int:pk>/update/',lead_update,name="lead_update"),
    path('<int:pk>/delete/',lead_delete,name="lead_delete"),
    path('create/',lead_create,name="lead_create")
    

]