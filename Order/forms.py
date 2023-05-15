from django import forms 
from .models import Order_detail

class Order_detail(forms.ModelForm):
    class Meta:
        model = Order_detail
        fields = ["Table_number","Number_Of_Person","Discount","item0","item_rate0","item_qty0","item_total0","item1","item_rate1","item_qty1","item_total1","item2","item_rate2","item_qty2","item_total2","item3","item_rate3","item_qty3","item_total3","item4","item_rate4","item_qty4","item_total4","item5","item_rate5","item_qty5","item_total5","item6","item_rate6","item_qty6","item_total6","item7","item_rate7","item_qty7","item_total7","item8","item_rate8","item_qty8","item_total8","item8","item_rate8","item_qty8","item_total8","item9","item_rate9","item_qty9","item_total9","total","Order_date","Order_Status",]
        labels = {"Table_number":"Table Number","Discount":"Discount","Number_Of_Person":"Total Person","total":"Total",}
    