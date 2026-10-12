from django.shortcuts import render 
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

def bscs(request): 
 return HttpResponse("<h2> Hello BSCS!</h2>") 
def indexPage(request): 
  return render(request, 'index.html')
def addNum(request):
  return render(request,"addNumbers.html")
 
def addNumsForm(request): 
  return render(request ,'addNumbers.html')
def addNumsResult(request):
    num1=float(request.GET['num1'])
    num2=float(request.GET['num2']) 
    res=num1+num2
    return render(request ,'addNumberResult.html',{'result':res})

# Create your views here.
from . forms import InsertForm
def insertForm(request):
   frm= InsertForm()
   return render(request,"insertForm.html",{'form':frm})


def createInsertProductView(response):
 if response.method =='POST':
  form =ProductForm(response.POST)
  if form.is_valid():
   product =form.save()
   return render(response,'message.html',{'msg':'Successful Insertion'})
  else:
    return render(response,'ProductForm.html',{'form':form})
 else:
    form =ProductForm()
    return render(response,'ProductForm.html',{'form':form})
 
def showAll(request): 
  allProducts = Product.objects.all()
  return render(request ,'showAllProducts.html',{'allProducts':allProducts})

def deleteProduct(request):
   id=request.GET['id']
   product = Product.objects.get(p_id=id)
   if product.delete():
      msg ={'msg':"Delete Successfully"}
   else: 
      msg ={'msg':"Not Delete"}
      return render(request,'message.html',{'msg':msg})
   return redirect('../showAll/')

def updateProduct(request):
    id = request.GET['id']
    product = Product.objects.get(p_id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('../showAll/')
    else:
        form = ProductForm(instance=product)

    return render(request, 'updateProduct.html', {'form': form})