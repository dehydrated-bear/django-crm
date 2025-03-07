from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import generic  
from .models import Lead,Agent,Category
from .forms import LeadForm,LeadModelForm,CustomUserCreation,AssignAgentForm,LeadCategoryUpdateForm
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import organisorandLoginRequiredMixin
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
#CRUD-- create ,retrive,update,delete +list

class SignupView(generic.CreateView):
    template_name="registration/signup.html"
    form_class=CustomUserCreation

    def get_success_url(self):
        return reverse("login")





class  landingpageview (generic.TemplateView):
    template_name="leads/landing_page.html"


def landing_page(request):

    return render(request,"leads/landing_page.html")

class LeadListView(LoginRequiredMixin , generic.ListView):
    template_name="leads/lead_list.html"
    context_object_name="lead"
    
    def get_queryset(self):
        user=self.request.user

        if user.is_organisor:
            queryset=Lead.objects.filter(organisation=user.userprofile , agent__isnull=False)

        else:
            queryset=Lead.objects.filter(organisation=user.agent.organisation , agent__isnull=False)

            #filter for the agent that is logged in
            queryset=queryset.filter(agent__user=user)

        return queryset
    
    def get_context_data(self,**kwargs):
        user=self.request.user
        context=super(LeadListView,self).get_context_data(**kwargs)
        if user.is_organisor:
            queryset=Lead.objects.filter(
                organisation=user.userprofile,
                agent__isnull=True
            )
            context.update({
                "unassigned_lead": queryset
            })
       
        return context

    #by default object_list is assigned to the queryset name
    


def lead_list(request):
    lead=Lead.objects.all()

    context={"lead":lead}
    # return HttpResponse("hello world")
    return render(request,"leads/lead_list.html",context)


class LeadDetailView(LoginRequiredMixin ,generic.DetailView):
    template_name="leads/lead_details.html"
    context_object_name="leads"

    def get_queryset(self):
        user=self.request.user

        if user.is_organisor:
            queryset=Lead.objects.filter(organisation=user.userprofile)

        elif user.is_agent:
            queryset=Lead.objects.filter(organisation=user.agent.organisation)

            #filter for the agent that is logged in
            queryset=queryset.filter(agent__user=user)

        return queryset

def lead_view(request,pk):
    print(pk)
    lead=Lead.objects.get(id=pk)
    context={
        "leads":lead
    }
    # return HttpResponse(f"here's the detail view {lead}")
    return render(request,"leads/lead_details.html",context)

class LeadCreateView(organisorandLoginRequiredMixin ,generic.CreateView):
    template_name="leads/lead_create.html"
    form_class=LeadModelForm

    def get_success_url(self):
        # return redirect("/leads")
        return reverse("leads:lead_list")
    
    def form_valid(self,form):

        lead=form.save(commit=False)
        lead.organisation=self.request.user.userprofile
        lead.save()

        # TODO send email
        send_mail(subject="a new lead has been created" , 
                  message="go to the site to see the neww lead",
                  from_email="test@test.com",
                  recipient_list=["test2@test.com"])

        return super(LeadCreateView,self).form_valid(form)

    



def lead_create(request):
    form=LeadModelForm()
    
    if request.method=="POST":
        print("recieving post request")
        form=LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context={
        "form":form
    }
    return render(request,"leads/lead_create.html",context)

class LeadUpdateView(organisorandLoginRequiredMixin ,generic.UpdateView):
    template_name="leads/lead_update.html"
    form_class=LeadModelForm
    
    
    context_object_name="lead"

    def get_queryset(self):
        user=self.request.user


        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse("leads:lead_list")



def lead_update(request,pk):
    
    lead=Lead.objects.get(id=pk)
    form=LeadModelForm(instance=lead)
    if request.method=="POST":
        
       
        form=LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")

            
            
            
    
    context={
        'lead':lead,
        'form':form
        }
    
    return render(request,"leads/lead_update.html",context)


class DeleteView(organisorandLoginRequiredMixin ,generic.DeleteView):
    template_name="leads/lead_delete.html"
    
    
    def get_success_url(self):
            return reverse("leads:lead_list") 
    
    def get_queryset(self):
        user=self.request.user


        return Lead.objects.filter(organisation=user.userprofile)

def lead_delete(request,pk):
    lead=Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")



class AssignAgentView(organisorandLoginRequiredMixin, generic.FormView):
    template_name="leads/assign_agent.html"
    form_class=AssignAgentForm

    def get_form_kwargs(self,**kwargs):
        kwargs=super(AssignAgentView,self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request":self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse("leads:lead_list")

    def form_valid(self,form):
        agent=form.cleaned_data["agent"]
        lead=Lead.objects.get(id=self.kwargs["pk"])
        lead.agent=agent
        lead.save()
        return super(AssignAgentView,self).form_valid(form)



class CategoryListView(LoginRequiredMixin,generic.ListView):
    template_name="leads/category_list.html"
    context_object_name="category_list"

    def get_context_data(self, **kwargs):
        context= super(CategoryListView,self).get_context_data(**kwargs)
        user=self.request.user

        if user.is_organisor:
            queryset=Lead.objects.filter(organisation=user.userprofile )

        else:
            queryset=Lead.objects.filter(organisation=user.agent.organisation )

        context.update({
            "unassigned_lead_count":queryset.filter(category__isnull=True).count()
        })

        return context


    def get_queryset(self):
        user=self.request.user

        if user.is_organisor:
            queryset=Category.objects.filter(organisation=user.userprofile )

        else:
            queryset=Category.objects.filter(organisation=user.agent.organisation )

           

        return queryset


class CategoryDetailView(LoginRequiredMixin,generic.DetailView):
    template_name="leads/category_detail.html"
    context_object_name="category"


    def get_queryset(self):
        user=self.request.user

        if user.is_organisor:
            queryset=Category.objects.filter(organisation=user.userprofile )

        else:
            queryset=Category.objects.filter(organisation=user.agent.organisation )

           

        return queryset
    
   
    
    def get_context_data(self, **kwargs):
        context= super(CategoryDetailView,self).get_context_data(**kwargs)
        
        # qs=Lead.objects.filter(category=self.get_object())
        #both of these do the same thing
        
        leads=self.get_object().leads.all()

        

        context.update({
            "leads":leads
        })

        return context

class LeadCategoryUpdateView(LoginRequiredMixin,generic.UpdateView):

    template_name="leads/lead_category_update.html"
    form_class=LeadCategoryUpdateForm
    
    
    context_object_name="lead"

    

    def get_success_url(self):
        return reverse("leads:lead_view" , kwargs={"pk":self.get_object().id})


    def get_queryset(self):
            user=self.request.user

            if user.is_organisor:
                queryset=Lead.objects.filter(organisation=user.userprofile)

            elif user.is_agent:
                queryset=Lead.objects.filter(organisation=user.agent.organisation)

                #filter for the agent that is logged in
                queryset=queryset.filter(agent__user=user)

            return queryset
    






# def lead_update(request,pk):
#     form=LeadForm()
#     lead=Lead.objects.get(id=pk)
#     if request.method=="POST":
        
#         form=LeadForm(request.POST)
#         if form.is_valid():
#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             age=form.cleaned_data['age']
            
#             lead.first_name=first_name
#             lead.last_name=last_name
#             lead.age=age
#             lead.save()

#             return redirect("/leads")
            
            
#     # if request.method=="POST":
#     context={
#         'lead':lead,
#         'form':form
#         }
    
#     return render(request,"leads/lead_update.html",context)




# def lead_create(request):
#     form=LeadForm()
    
    # if request.method=="POST":
    #     print("recieving post request")
    #     form=LeadForm(request.POST)
    #     if form.is_valid():
    #         print("the form is valid")
    #         print(form.cleaned_data)
    #         first_name=form.cleaned_data['first_name']
    #         last_name=form.cleaned_data['last_name']
    #         age=form.cleaned_data['age']
    #         agent=Agent.objects.first()
    #         Lead.objects.create(
    #             first_name=first_name,
    #             last_name=last_name,
    #             age=age,
    #             agent=agent
    #         )
    #         return redirect("/leads")

#     context={
#         "form":form
#     }
#     return render(request,"leads/lead_create.html",context)