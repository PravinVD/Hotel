from django.shortcuts import render,HttpResponse
from .forms import Order_detail
from .models import Order_detail as Create_order
from Shop_detail.models import Product_detail,Shop_Detail
import datetime

# Create your views here.
def create_order(request):
    list_product = Product_detail.objects.all()
    if request.method == 'POST':
        Table_number = int(request.POST['Table_number'])
        Number_Of_Person = int(request.POST['Number_Of_Person'])
        Discount = int(request.POST['Discount'])
        item0 = request.POST['item0']
        item_qty0 = int(request.POST['item_qty0'])
        item_rate0 = Product_detail.objects.get(item_name=item0)
        item_rate0 = int(item_rate0.item_rate)
        item_total0 = item_rate0 * item_qty0
        item1 = request.POST['item1']
        item_qty1 = int(request.POST['item_qty1'])
        item_rate1 = Product_detail.objects.get(item_name=item1)
        item_rate1 = int(item_rate1.item_rate)
        item_total1 = item_rate1 * item_qty1
        item2 = request.POST['item2']
        item_qty2 = int(request.POST['item_qty2'])
        item_rate2 = Product_detail.objects.get(item_name=item2)
        item_rate2 = int(item_rate2.item_rate)
        item_total2 = item_rate2 * item_qty2
        item3 = request.POST['item3']
        item_qty3 = int(request.POST['item_qty3'])
        item_rate3 = Product_detail.objects.get(item_name=item3)
        item_rate3 = int(item_rate3.item_rate)
        item_total3 = item_rate3 * item_qty3
        item4 = request.POST['item4']
        item_qty4 = int(request.POST['item_qty4'])
        item_rate4 = Product_detail.objects.get(item_name=item4)
        item_rate4 = int(item_rate4.item_rate)
        item_total4 = item_rate4 * item_qty4
        item5 = request.POST['item5']
        item_qty5 = int(request.POST['item_qty5'])
        item_rate5 = Product_detail.objects.get(item_name=item5)
        item_rate5 = int(item_rate5.item_rate)
        item_total5 = item_rate5 * item_qty5
        item6 = request.POST['item6']
        item_qty6 = int(request.POST['item_qty6'])
        item_rate6 = Product_detail.objects.get(item_name=item6)
        item_rate6 = int(item_rate6.item_rate)
        item_total6 = item_rate6 * item_qty6
        item7 = request.POST['item7']
        item_qty7 = int(request.POST['item_qty7'])
        item_rate7 = Product_detail.objects.get(item_name=item7)
        item_rate7 = int(item_rate7.item_rate)
        item_total7 = item_rate7 * item_qty7
        item8 = request.POST['item8']
        item_qty8 = int(request.POST['item_qty8'])
        item_rate8 = Product_detail.objects.get(item_name=item8)
        item_rate8 = int(item_rate8.item_rate)
        item_total8 = item_rate8 * item_qty8
        item9 = request.POST['item9']
        item_qty9 = int(request.POST['item_qty9'])
        item_rate9 = Product_detail.objects.get(item_name=item9)
        item_rate9 = int(item_rate9.item_rate)
        item_total9 = item_rate9 * item_qty9
        total = item_total0 + item_total1 + item_total2 + item_total3 + item_total4 + item_total5 + item_total6 + item_total7 + item_total8 + item_total9
        if Discount != 0:
            count = (total/100)*Discount
            total = total - count
        else:
            total
        Order_date = datetime.datetime.now()
        Sample = Create_order(Table_number=Table_number,Number_Of_Person=Number_Of_Person,Discount=Discount,
                              item0=item0,item_qty0=item_qty0,item_rate0=item_rate0,item_total0=item_total0,
                              item1=item1,item_qty1=item_qty1,item_rate1=item_rate1,item_total1=item_total1,
                              item2=item2,item_qty2=item_qty2,item_rate2=item_rate2,item_total2=item_total2,
                              item3=item3,item_qty3=item_qty3,item_rate3=item_rate3,item_total3=item_total3,
                              item4=item4,item_qty4=item_qty4,item_rate4=item_rate4,item_total4=item_total4,
                              item5=item5,item_qty5=item_qty5,item_rate5=item_rate5,item_total5=item_total5,
                              item6=item6,item_qty6=item_qty6,item_rate6=item_rate6,item_total6=item_total6,
                              item7=item7,item_qty7=item_qty7,item_rate7=item_rate7,item_total7=item_total7,
                              item8=item8,item_qty8=item_qty8,item_rate8=item_rate8,item_total8=item_total8,
                              item9=item9,item_qty9=item_qty9,item_rate9=item_rate9,item_total9=item_total9,
                              total=total,Order_date=Order_date,)
        Sample.save()
        return HttpResponse("Form Saved")
    form = Order_detail()
    context = {'form':form,'list_product':list_product,}
    return render(request,"Order/create_order.html",context)

def Open_order(request):
    orders = Create_order.objects.all()
    return render(request,"Order/Open_order.html",{'orders':orders,})

def Close_order(request):
    orders = Create_order.objects.all()
    return render(request,"Order/Close_order.html",{'orders':orders,})

#edit order views here

# Create your views here.
def edit_order(request,id):
    update_order = Create_order.objects.get(pk=id)
    list_product = Product_detail.objects.all()
    if request.method == 'POST':
        update_order.Table_number = int(request.POST['Table_number'])
        update_order.Number_Of_Person = int(request.POST['Number_Of_Person'])
        update_order.Discount = int(request.POST['Discount'])
        update_order.item0 = request.POST['item0']
        update_order.item_qty0 = int(request.POST['item_qty0'])
        update_order.item_rate0 = Product_detail.objects.get(item_name=update_order.item0)
        update_order.item_rate0 = int(update_order.item_rate0.item_rate)
        update_order.item_total0 = update_order.item_rate0 * update_order.item_qty0
        update_order.item1 = request.POST['item1']
        update_order.item_qty1 = int(request.POST['item_qty1'])
        update_order.item_rate1 = Product_detail.objects.get(item_name=update_order.item1)
        update_order.item_rate1 = int(update_order.item_rate1.item_rate)
        update_order.item_total1 = update_order.item_rate1 * update_order.item_qty1
        update_order.item2 = request.POST['item2']
        update_order.item_qty2 = int(request.POST['item_qty2'])
        update_order.item_rate2 = Product_detail.objects.get(item_name=update_order.item2)
        update_order.item_rate2 = int(update_order.item_rate2.item_rate)
        update_order.item_total2 = update_order.item_rate2 * update_order.item_qty2
        update_order.item3 = request.POST['item3']
        update_order.item_qty3 = int(request.POST['item_qty3'])
        update_order.item_rate3 = Product_detail.objects.get(item_name=update_order.item3)
        update_order.item_rate3 = int(update_order.item_rate3.item_rate)
        update_order.item_total3 = update_order.item_rate3 * update_order.item_qty3
        update_order.item4 = request.POST['item4']
        update_order.item_qty4 = int(request.POST['item_qty4'])
        update_order.item_rate4 = Product_detail.objects.get(item_name=update_order.item4)
        update_order.item_rate4 = int(update_order.item_rate4.item_rate)
        update_order.item_total4 = update_order.item_rate4 * update_order.item_qty4
        update_order.item5 = request.POST['item5']
        update_order.item_qty5 = int(request.POST['item_qty5'])
        update_order.item_rate5 = Product_detail.objects.get(item_name=update_order.item5)
        update_order.item_rate5 = int(update_order.item_rate5.item_rate)
        update_order.item_total5 = update_order.item_rate5 * update_order.item_qty5
        update_order.item6 = request.POST['item6']
        update_order.item_qty6 = int(request.POST['item_qty6'])
        update_order.item_rate6 = Product_detail.objects.get(item_name=update_order.item6)
        update_order.item_rate6 = int(update_order.item_rate6.item_rate)
        update_order.item_total6 = update_order.item_rate6 * update_order.item_qty6
        update_order.item7 = request.POST['item7']
        update_order.item_qty7 = int(request.POST['item_qty7'])
        update_order.item_rate7 = Product_detail.objects.get(item_name=update_order.item7)
        update_order.item_rate7 = int(update_order.item_rate7.item_rate)
        update_order.item_total7 = update_order.item_rate7 * update_order.item_qty7
        update_order.item8 = request.POST['item8']
        update_order.item_qty8 = int(request.POST['item_qty8'])
        update_order.item_rate8 = Product_detail.objects.get(item_name=update_order.item8)
        update_order.item_rate8 = int(update_order.item_rate8.item_rate)
        update_order.item_total8 = update_order.item_rate8 * update_order.item_qty8
        update_order.item9 = request.POST['item9']
        update_order.item_qty9 = int(request.POST['item_qty9'])
        update_order.item_rate9 = Product_detail.objects.get(item_name=update_order.item9)
        update_order.item_rate9 = int(update_order.item_rate9.item_rate)
        update_order.item_total9 = update_order.item_rate9 * update_order.item_qty9
        total = [update_order.item_total0,update_order.item_total1,update_order.item_total2,update_order.item_total3,update_order.item_total4,update_order.item_total5,update_order.item_total6,update_order.item_total7,update_order.item_total8,update_order.item_total9]
        update_order.total = sum(total)
        if update_order.Discount == 0:
            update_order.total
            print(update_order.total)
        else:
            count = (update_order.total/100)*update_order.Discount
            update_order.total = update_order.total - count
        update_order.Order_date = datetime.datetime.now()
        update_order.save(update_fields=['Table_number','Number_Of_Person','Discount',
                              'item0','item_qty0','item_rate0','item_total0',
                              'item1','item_qty1','item_rate1','item_total1',
                              'item2','item_qty2','item_rate2','item_total2',
                              'item3','item_qty3','item_rate3','item_total3',
                              'item4','item_qty4','item_rate4','item_total4',
                              'item5','item_qty5','item_rate5','item_total5',
                              'item6','item_qty6','item_rate6','item_total6',
                              'item7','item_qty7','item_rate7','item_total7',
                              'item8','item_qty8','item_rate8','item_total8',
                              'item9','item_qty9','item_rate9','item_total9',
                              'total','Order_date',])
        return HttpResponse("Form updated")
    form = Order_detail()
    context = {'form':form,'list_product':list_product,'update_order':update_order,}
    return render(request,"Order/edit_order.html",context)

def view_order(request,id):
    order = Create_order.objects.get(pk=id)
    Shop = Shop_Detail.objects.get(pk=1)
    context = {'order':order,'Shop':Shop,}
    
    return render(request,"Order/view_order.html",context)

def print_order(request,id):
    order = Create_order.objects.get(pk=id)
    order.Order_Status = "CLOSED"
    order.save(update_fields=['Order_Status',])
    Shop = Shop_Detail.objects.get(pk=1)
    context = {'order':order,'Shop':Shop,}
    
    return render(request,"Order/print1.html",context)
def cancel_order(request,id):
    order = Create_order.objects.get(pk=id)
    order.delete()
    return HttpResponse("order Deleted")
    
    
