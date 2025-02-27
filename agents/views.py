import random
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from django.shortcuts import reverse
from .forms import AgentModelForm
from.mixins import organisorandLoginRequiredMixin
from  django.core.mail import send_mail


# Create your views here.


class AgentListView(organisorandLoginRequiredMixin,generic.ListView):

    template_name='agents/agent_list.html'


    def get_queryset(self):
        organization= self.request.user.userprofile
        return Agent.objects.filter(organisation=organization)
    
class AgentCreateView(organisorandLoginRequiredMixin,generic.CreateView):
    template_name="agents/agent_create.html"

    form_class=AgentModelForm

    def get_success_url(self):

        return  reverse("agents:agent_list")
    
    def form_valid(self,form):

        user=form.save(commit=False)
        user.is_agent=True
        user.is_organisor=False
        user.set_password(f"{random.randint(0,1000000)}")
        user.save()
        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile,
            
        )

        send_mail(
            subject="youu were invited to be an agent",
            message="ypu werer added as  a agent in the django crm please login",
            from_email="admin@test.com",
            recipient_list=[user.email],

        )
        return super(AgentCreateView,self).form_valid(form)


class AgentDetailView(organisorandLoginRequiredMixin,generic.DetailView):

    template_name="agents/agent_detail.html"
    context_object_name="agent"

    def get_queryset(self):
        organization= self.request.user.userprofile
        return Agent.objects.filter(organisation=organization)

class AgentUpdateView(organisorandLoginRequiredMixin,generic.UpdateView):
    template_name="agents/agent_update.html"
    form_class=AgentModelForm
    

    def get_success_url(self):
        return reverse("agents:agent_list")
    
    def get_queryset(self):
        organization= self.request.user.userprofile
        return Agent.objects.filter(organisation=organization)
    
class AgentDeleteView(organisorandLoginRequiredMixin,generic.DeleteView):
    template_name="agents/agent_delete.html"

    def get_success_url(self):
        return reverse("agents:agent_list")
    
    def get_queryset(self):
        organization= self.request.user.userprofile
        return Agent.objects.filter(organisation=organization)
    