from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import GroceryItem
import datetime 
# Create your views here.
def index(request):
    items=GroceryItem.objects.filter(user_id=request.user).order_by('-date',)
    return render(request,'index.html',{'items':items,'curr':'All Data'})

def signUp(request):
    if request.method=='POST':
        name=request.POST['signupname']
        email=request.POST['signupemail']
        password=request.POST['signuppassword']
        password=request.POST['signuppassword']
        cpassword=request.POST['signupcpassword']

        #Check Conditions
        if password != cpassword:
            messages.error(request,"Password doesn't match")
            return redirect('/')
        myUser=User.objects.create_user(email,email,password)
        myUser.first_name=name
        myUser.save()
        messages.success(request,"Your account has been successfuly created")
        return redirect('/')
    else:
        return HttpResponse("404 - Not Found")
def logIn(request):
    if request.method=='POST':
        username=request.POST['loginemailid']
        password=request.POST['loginpassword']
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('/')

def logOut(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('/')

def addItem(request):
    if request.method=='POST':
        itemname=request.POST['itemname']
        quantity=request.POST['itemquantity']
        status=request.POST['status']
        date=request.POST['date']
        item=GroceryItem(item_name=itemname,item_quantity=quantity,item_status=status,user_id=request.user,date=date)
        item.save()
        messages.success(request,"New Item Added Successfully!!")
        return redirect('/')
    else:
        return redirect('/')

def filter(request):
    if request.method=='POST':
        date=request.POST['date']
        if date is '':
            items=GroceryItem.objects.filter(user_id=request.user,date=datetime.datetime.now().date()).order_by('-date',)
            return render(request,'index.html',{'items':items,'curr':'All'})
        else:
            items=GroceryItem.objects.filter(user_id=request.user,date=date).order_by('-date',)
            curr=""
            for i in items:
                curr=i.date
                break
            return render(request,'index.html',{'items':items,'curr':date})
    else:
        return redirect('/')

def delete(request,id):
    demp=GroceryItem.objects.get(id=id)
    demp.delete()
    return redirect('/')

def update(request,id):
    data=GroceryItem.objects.get(id=id)
    print(data.item_name)
    print(data.item_quantity)
    print(type(data.item_status))
    return render(request,'update.html',{'data':data})

def finalupdate(request):
    if request.method=='POST':
        cid=request.POST['custId']
        itemname=request.POST['itemname']
        quantity=request.POST['itemquantity']
        status=request.POST['status']
        date=request.POST['date']
        demp=GroceryItem.objects.get(id=int(cid))
        demp.delete()
        item=GroceryItem(item_name=itemname,item_quantity=quantity,item_status=status,user_id=request.user,date=date)
        item.save()
        messages.success(request,"Item Updated")
        return redirect('/')