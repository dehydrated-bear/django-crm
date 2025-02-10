from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Lead,Agent
from .forms import LeadForm,LeadModelForm

# Create your views here.

def landing_page(request):

    return render(request,"leads/landing_page.html")


def lead_list(request):
    lead=Lead.objects.all()

    context={"lead":lead}
    # return HttpResponse("hello world")
    return render(request,"leads/lead_list.html",context)

def lead_view(request,pk):
    print(pk)
    lead=Lead.objects.get(id=pk)
    context={
        "leads":lead
    }
    # return HttpResponse(f"here's the detail view {lead}")
    return render(request,"leads/lead_details.html",context)

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