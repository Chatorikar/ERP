'''
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views

from . import views

urlpatterns = [
   
    path('all/', views.final_product_list, name='product_list'),
    url(r'^get_components/(?P<final_product_id>\d+)/$', views.final_product_components_by_id),
    url(r'^get_component_info/(?P<component_id>\d+)/$', views.components_list_id),
    path('create_product/', views.create_product),
    url(r'^create_component/(?P<final_product_id>\d+)/$', views.create_component),
]

'''

from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views
from . import views

urlpatterns = [

    path('all/', views.final_product_list, name='product_list'),
    path('rm/', views.Inventary, name='Inventary'),
    path('Create_Raw_Material/', views.Create_Raw_Material,
         name='Create_Raw_Material'),
    url(r'^Assign_Raw_Material/(?P<component_id>\d+)/$', views.Assign_Raw_Material),
    url(r'^Update_Raw_Material/(?P<component_id>\d+)/$',
        views.update_quantity_raw_material),

    path('ayushi/', views.ayushi, name='ayushi'),

    url(r'^get_components/(?P<final_product_id>\d+)/$',
        views.final_product_components_by_id),
    url(r'^get_component_info/(?P<component_id>\d+)/$',
        views.get_components_details),
    url(r'^create_component/(?P<final_product_id>\d+)/$', views.create_component),
    url(r'^delete_component/(?P<component_id>\d+)/(?P<final_product_id>\d+)/$',
        views.delete_component, name='delete_component'),

    url(r'^create_product/', views.create_product),
    url(r'^delete_Final_Product/(?P<final_product_id>\d+)/$',
        views.delete_Final_Product, name='delete_Final_Product'),






    #path('create_process/', views.get_process_details_paticular_component),

    url(r'^Add_Process_to_Component/(?P<component_id>\d+)/$',
        views.Add_Process_to_Component),
    url(r'^get_porcess_info/(?P<component_id>\d+)/$', views.create_process),

    url(r'^change_process_status/(?P<component_id>\d+)/$',
        views.change_process_status),



]
