from django.urls import path

from .views import (LeadListView,LeadDetailView,LeadCreateView,
                    LeadUpdateView,DeleteView,AssignAgentView,
                    CategoryListView,CategoryDetailView,LeadCategoryUpdateView)

app_name="leads"

urlpatterns=[
    path('',LeadListView.as_view(),name="lead_list"),
    path('<int:pk>/',LeadDetailView.as_view(),name="lead_view"),
    path('<int:pk>/update/',LeadUpdateView.as_view(),name="lead_update"),
    path('<int:pk>/delete/',DeleteView.as_view(),name="lead_delete"),
    path('create/',LeadCreateView.as_view(),name="lead_create"),
    path('<int:pk>/assign-agent/',AssignAgentView.as_view(),name="assign_agent"),
    path('<int:pk>/category/',LeadCategoryUpdateView.as_view(),name="lead_category_update"),
    path('categories/',CategoryListView.as_view(),name="category_list"),
    path('categories/<int:pk>/',CategoryDetailView.as_view(),name="category_detail")
    

]