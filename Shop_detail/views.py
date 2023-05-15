from django.shortcuts import render,HttpResponse,redirect
from .models import Shop_Detail,Product_detail
from .forms import Shop_Details,Product_details
from django.contrib.auth import authenticate


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request,"Shop_detail/dashboard.html")
    else:
        return redirect("login")

def add_shop_detail(request):
    Shop_Detailss = Shop_Detail.objects.get(pk=1)
    print(Shop_Detailss.Shop_Name)
    if request.method == 'POST':
        form = Shop_Details(request.POST,instance=Shop_Detailss)
        if form.is_valid():
            form.save()
            return HttpResponse("form Submitted Sucessfully")
    form = Shop_Details()
    return render(request,"Shop_detail/add_shop_detail.html",{'form':form,'Shop_Detailss':Shop_Detailss})

def add_product(request):
    if request.method == 'POST':
        form = Product_details(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Product Added")
    form = Product_details()
    return render(request,"Shop_detail/add_product.html",{'form':form})

def edit_product(request,id):
    list_product = Product_detail.objects.all()
    context = {'list_product':list_product,}
    Product_detailss = Product_detail.objects.get(pk=id)
    if request.method == 'POST':
        form = Product_details(request.POST,instance= Product_detailss)
        if form.is_valid():
            form.save()
            return render(request,"Shop_detail/list_product.html",context)
    form = Product_details(instance=Product_detailss)
    context = {'form':form,'Product_detailss':Product_detailss,}
    return render(request,"Shop_detail/edit_product.html",context)

def list_product(request):
    list_product = Product_detail.objects.all()
    context = {'list_product':list_product,}
    return render(request,"Shop_detail/list_product.html",context)
    
def del_product(request,id):
    find_Delete_product = Product_detail.objects.get(pk=id)
    if find_Delete_product.item_name != "Select":
        find_Delete_product.delete()
    list_product = Product_detail.objects.all()
    context = {'list_product':list_product,}
    return render(request,"Shop_detail/list_product.html",context)