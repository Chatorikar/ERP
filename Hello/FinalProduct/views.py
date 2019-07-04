from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import Context
from django.template.loader import get_template
from .models import *
from . forms import *
from django.template.context_processors import csrf

# Final Product----------------------------------------
def create_product(request):
    if request.POST:
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/fp/all')
    else:
        form = CreateProduct()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    args.update({'final_products': Finalproduct.objects.all()})
    return render_to_response('create_product.html', args)

def final_product_list(request):
    return render_to_response('final_products.html', {'final_products': Finalproduct.objects.all()})

def final_product_components_by_id(request, final_product_id=1):
    components = Finalproduct.objects.get(id=final_product_id).component_list.all()
    return render_to_response('all_components.html', {'components': components, 'final_product_id':final_product_id , 'model':Finalproduct.objects.get(id=final_product_id)})



# For Componenets
def create_component(request, final_product_id=1):
    if request.POST:
        form = CreateComponent(request.POST, request.FILES)
        form_1 = CreateComponent()
        if form.is_valid():               
            form.save()
            Finalproduct.objects.get(id=final_product_id).component_list.add(Components.objects.latest('pk'))
            #Will add Recentaly add new components object from Components Class
            return HttpResponseRedirect('/fp/get_components/' + str(final_product_id))
    else:
        form = CreateComponent()
    args = {}
    args.update(csrf(request))
    args.update({'form':form}) 
    args.update({'model':Finalproduct.objects.get(id=final_product_id)})
    args['components'] = Finalproduct.objects.get(id=final_product_id).component_list.all()
    return render_to_response('create_components.html', args)

def components_list_id(request, components_id=1):
    return render_to_response('get_by_id.html', {'component': Components.objects.get(id=component_id), 'component_id': components_id})





######################## Add process 


def create_process(request, component_id=1):
    if request.POST:
        form = CreateProcess(request.POST, request.FILES)
        form_1 = CreateProcess()
        if form.is_valid():               
            form.save()
            Components.objects.get(id=component_id).process_list.add(Process.objects.latest('pk'))
            #Will add Recentaly add new components object from Components Class
            return HttpResponseRedirect('/fp/get_component_info/' + str(component_id))
    else:
        form = CreateProcess()
    args = {}
    args.update(csrf(request))
    args.update({'form':form}) 
    args.update({'component':Components.objects.get(id=component_id)})
    args['process'] = Components.objects.get(id=component_id).process_list.all()
    return render_to_response('process_list_of_particular_component.html', args)

def get_components_details(request, component_id=1):
    return render_to_response('get_components_details.html', {'component': Components.objects.get(id=component_id), 'component_id': component_id , 'All_Process': Components.objects.get(id=component_id).process_list.all()})


def get_process_details_paticular_component(request , component_id=1 ):
    return render_to_response('process_list_of_particular_component.html', {'All_Process' : Components.objects.get(id=component_id).process_list.all() ,'component': Components.objects.get(id=component_id) })















'''
def index(request):
    name = "Prathamesh"
    html = "<html><body> Hi %s This seems to be Worked </body></html>" % name
    return HttpResponse(html)


def hello_templates(request):
    # print("In Final Product")
    name = "Prathamesh"
    # temp = get_template('hello.html')
    # html = temp.render(Context())
    # #return HttpResponse(html)
    return render_to_response('hello.html', {'name': name} )
'''