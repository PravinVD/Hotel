from django import forms 
from .models import Shop_Detail,Product_detail

class Shop_Details(forms.ModelForm):
    class Meta:
        model = Shop_Detail
        fields = ["Shop_Name","Shop_address","Number",]
        labels = {"Shop_Name":"Shop Name","Shop_address":"Shop address","Number":"Number",}

class Product_details(forms.ModelForm):
    class Meta:
        model = Product_detail
        fields =["item_name","item_rate",]
        labels = {"item_name":"Item Name","item_rate":"Item Rate",}
        widgets = {
            "item_name":forms.TextInput(attrs={'class':'form-control '}),
            "item_rate":forms.TextInput(attrs={'class':'form-control '}),
        }
    