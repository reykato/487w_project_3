from django.shortcuts import render, redirect
from django.http import Http404
from .models import *
from .forms import *

def view_requests(request):
    requests = Maintenance_Request.objects.all()
    context = {'requests' : requests}
    return render(request, 'tenant_page.html', context)

def new_request(request):
    req = Maintenance_Request(status="Pending")
    form = Request_Form(instance=req)
    if request.method == 'POST':
        form = Request_Form(request.POST, request.FILES, instance=req)
        if form.is_valid():            
            form.save()
            return redirect('/')
        else:
            raise Http404('Invalid Request Entered')

    context = {'form': form}
    return render(request, 'new_request.html', context)

def view_tenants(request):
    tenants = Tenant.objects.all()
    context = {'tenants' : tenants}
    return render(request, 'manager_page.html', context)

def new_tenant(request):
    form = Tenant_Form()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            for error in form.errors:
                print(error)
            raise Http404("Invalid Tenant Information Entered" + str(form.errors))
    
    context = {'form': form}
    return render(request, 'new_tenant.html', context)

def edit_tenant(request, pk):
    tenant = Tenant.objects.get(id=pk)
    form = Tenant_Form(instance=tenant)
    if request.method == 'POST':
        form = Tenant_Form(request.POST, instance = tenant)
        if form.is_valid():
            form.save()
            return redirect('tenants')
        else:
            raise Http404("Invalid Tenant Information Entered" + str(form.errors))

    context = {'form' : form}
    return render(request, 'edit_tenant.html', context)

def delete_tenant(request, pk):
    Tenant.objects.filter(id=pk).delete()
    return redirect('/tenants')

def maintenance_view(request):
    requests = Maintenance_Request.objects.all()
    context = {'requests' : requests}
    return render(request, 'maintenance_page.html', context)

def change_request_status(request, pk):
    request = Maintenance_Request.objects.get(id=pk)
    request.status = "Completed"
    request.save()
    return redirect('/maintenance')