from django.urls import path
from .views import AgentListView,AgentCreateView

app_name='agent'

urlpatterns=[

    path('',AgentListView.as_view(),name="agent_list"),
    path('create/',AgentCreateView.as_view(),name="agent_create")

]