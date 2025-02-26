from django.urls import path
from .views import AgentListView,AgentCreateView,AgentDetailView,AgentUpdateView,AgentDeleteView

app_name='agent'

urlpatterns=[

    path('',AgentListView.as_view(),name="agent_list"),
    path('create/',AgentCreateView.as_view(),name="agent_create"),
    path('<int:pk>/',AgentDetailView.as_view(),name="agent_view"),
    path('<int:pk>/update/',AgentUpdateView.as_view(),name="agent_update"),
    path('<int:pk>/delete/',AgentDeleteView.as_view(),name="agent_delete")
]