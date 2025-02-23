from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import generic  
from .models import Lead,Agent
from .forms import LeadForm,LeadModelForm,CustomUserCreation
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
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
    queryset=Lead.objects.all()
    #by default object_list is assigned to the queryset name
    context_object_name="lead"

def lead_list(request):
    lead=Lead.objects.all()

    context={"lead":lead}
    # return HttpResponse("hello world")
    return render(request,"leads/lead_list.html",context)


class LeadDetailView(LoginRequiredMixin ,generic.DetailView):
    template_name="leads/lead_details.html"
    queryset=Lead.objects.all()
    context_object_name="leads"


def lead_view(request,pk):
    print(pk)
    lead=Lead.objects.get(id=pk)
    context={
        "leads":lead
    }
    # return HttpResponse(f"here's the detail view {lead}")
    return render(request,"leads/lead_details.html",context)

class LeadCreateView(LoginRequiredMixin ,generic.CreateView):
    template_name="leads/lead_create.html"
    form_class=LeadModelForm

    def get_success_url(self):
        # return redirect("/leads")
        return reverse("leads:lead_list")
    
    def form_valid(self,form):
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

class LeadUpdateView(LoginRequiredMixin ,generic.UpdateView):
    template_name="leads/lead_update.html"
    form_class=LeadModelForm
    queryset=Lead.objects.all()
    context_object_name="lead"

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


class DeleteView(LoginRequiredMixin ,generic.DeleteView):
    template_name="leads/lead_delete.html"
    queryset=Lead.objects.all()
    
    def get_success_url(self):
            return reverse("leads:lead_list") 

def lead_delete(request,pk):
    lead=Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
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