from django.urls import path 
from . import views 
urlpatterns = [
path('bscs-tag/', views.bscs, name='bscs'),
path('', views.indexPage, name='indexPage'),
path( 'addNums/',views.addNum),

path('addNumsForm/', views.addNumsForm),
path('addNumsResult/', views.addNumsResult),
path('insertinform/' , views.insertForm),

path("productForm/",views.createInsertProductView,name="createInsertProductView"),
path('showAll/', views.showAll, name='showAll'),
path('deleteProduct/', views.deleteProduct, name='deleteProduct'),
path('updateProduct/', views.updateProduct, name='updateProduct')
]