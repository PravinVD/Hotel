from django.shortcuts import render,HttpResponse
from Staff.forms import *
from Staff.models import *
from django.contrib.auth.models import User,Group
import datetime

# Create your views here.
def Create_staff(request):
    if request.method == 'POST':
        FN = request.POST['First_Name']
        LN = request.POST['Last_Name']
        PN = request.POST['Mobile_No']
        Add = request.POST['Address']
        CD = datetime.date.today()
        LD = datetime.date.today() + datetime.timedelta(days=10*365)
        LUD = datetime.date.today()
        User_Name = PN
        Password = request.POST['pass']
        new_password = request.POST['pass_confirm']
        if Password == new_password:
            U = User.objects.create_user(username=User_Name,first_name=FN,last_name=LN,password=Password,)
            U.save()
            gro = Group.objects.get(name="Staff_Owner")
            per = User.objects.get(username = User_Name)
            per.groups.add(gro)
            
            sample = staff_detail1(First_Name=FN,Last_Name=LN,Address=Add,Mobile_No=PN,Create_date=CD,Leave_date=LD,Last_update_Date=LUD)
            sample.save()
            return HttpResponse("UserProfile Created ")
        else:
            return HttpResponse("UserProfile Not Created ")
    form = Staff1()
    return render(request,"Staff/create_staff.html",{'form':form,})#{'form':form,}
def view_profile(request,id):
    sd1 = staff_detail1.objects.get(pk=id)
    return render(request,"Staff/view_profile.html",{'sd1':sd1})
def view_staff(request):
    sd = staff_detail1.objects.all()
    
    return render(request,"Staff/view_staff.html",{'sd':sd})

def edit_staff(request,id):
    Staff_d = staff_detail1.objects.get(pk=id)
    if request.method == 'POST':
        form = Staff1(request.POST,instance=Staff_d)
        
        if form.is_valid():
            form.save()
            return HttpResponse("form Submitted Sucessfully")
    form = Staff1(instance=Staff_d)
    return render(request,"Staff/edit_profile.html",{'form':form},)

def add_salary(request):
    sd = staff_detail1.objects.all()
    emp = []
    for each in sd:
        FL = each.First_Name + " " + each.Last_Name
        emp.append(FL)
    if request.method == 'POST':
        emp_name = request.POST['emp_name']
        sl = emp_name.split()
        st = staff_detail1.objects.get(First_Name = sl[0],Last_Name= sl[1])
        emp_no = st.pk
        amount_paid = request.POST['amount']
        Paid_date = request.POST['paid_date']
        if Paid_date == "":
            Paid_date = datetime.date.today()
        salary = Salary_model(Emp_No = emp_no,Emp_Name=emp_name,Amount_Paid = amount_paid,Amount_Paid_Date = Paid_date)
        salary.save()  
        return HttpResponse("Employee Salary Detail Added")      
    context = {'sd':sd,'emp':emp,}
  
    return render(request,"Staff/Emplyee_salary.html",context)

def view_salary(request,id):
    get_detail = Salary_model.objects.filter(Emp_No=id).order_by('pk')[::-1]
    return render(request,"Staff/view_salary.html",{'get_detail':get_detail})

def add_daily(request):
    form = Daily()
    return render(request,"Staff/add_daily.html",{'form':form})
