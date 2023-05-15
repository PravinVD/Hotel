from django import forms
from .models import staff_detail1,daily_expense

class Staff1(forms.ModelForm):
    class Meta:
        model = staff_detail1
        fields = ["First_Name","Last_Name","Mobile_No","Address","Create_date","Leave_date",]
        #labels = {"ID_Proof":"ID Proof",}
       
        widgets = {
            "First_Name":forms.TextInput(attrs={'type':'text','class':'form-control col'}),
            "Last_Name":forms.TextInput(attrs={'type':'text','class':'form-control col '}),
            "Mobile_No":forms.TextInput(attrs={'type':'text','class':'form-control col '}),
            "Address":forms.TextInput(attrs={'type':'text','class':'form-control col'}),
            "Create_date":forms.DateInput(attrs={'type':'date','class':'form-control col'}),
            "Leave_date":forms.DateInput(attrs={'type':'date','class':'form-control col'}),
        }
        
class Daily(forms.ModelForm):
    class Meta:
        model = daily_expense
        fields = ["Expense_date","description","Daily_Total",]
        labels = {"Expense_date":"DATE","description":"Add details","Daily_Total":"Today Total Expense",}
        widgets = {
            "description":forms.Textarea(attrs={'class':'form-control col-12'}),
            "Expense_date":forms.DateInput(attrs={'type':'date','class':'form-control col-12'}),
            "Daily_Total":forms.NumberInput(attrs={'type':'text','class':'form-control col-12 '}),
        }