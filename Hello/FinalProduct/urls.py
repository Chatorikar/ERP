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
    url(r'^get_components/(?P<final_product_id>\d+)/$', views.final_product_components_by_id),
    
    url(r'^get_component_info/(?P<component_id>\d+)/$', views.get_components_details),
    
    url(r'^create_product/', views.create_product),
    url(r'^create_component/(?P<final_product_id>\d+)/$', views.create_component),
    url(r'^create_process/(?P<component_id>\d+)/$', views.create_process),
    # path('create_process/', views.get_process_details_paticular_component),
    url(r'^get_porcess_info/(?P<component_id>\d+)/$', views.create_process),
]
