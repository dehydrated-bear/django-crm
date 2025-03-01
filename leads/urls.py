from django.urls import path

from .views import lead_list,lead_view,lead_create,lead_update,lead_delete,landing_page,LeadListView,LeadDetailView,LeadCreateView,LeadUpdateView,DeleteView,AssignAgentView

app_name="leads"

urlpatterns=[
    path('',LeadListView.as_view(),name="lead_list"),
    path('<int:pk>/',LeadDetailView.as_view(),name="lead_view"),
    path('<int:pk>/update/',LeadUpdateView.as_view(),name="lead_update"),
    path('<int:pk>/delete/',DeleteView.as_view(),name="lead_delete"),
    path('create/',LeadCreateView.as_view(),name="lead_create"),
    path('<int:pk>/assign-agent/',AssignAgentView.as_view(),name="assign_agent")
    

]