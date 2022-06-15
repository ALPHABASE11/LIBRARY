import datetime
from django.shortcuts import render,redirect
from manager.models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
            admininfo.objects.get(email=email,password=password)
            messages.success(request, 'Successfully Registered')
            return redirect('/book')
        except :
            messages.error(request, 'You Have Entered Invalid Email Id or Password')
            return redirect('/login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        name = request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        try:
            admininfo(name=name,email=email,password=password).save()
            messages.success(request, 'Successfully Registered')
            return redirect('/login')
        except:
            messages.error(request,'Email Entered Have Already Registered Try Different Email')
            return redirect('/register')
    return render(request,'register.html')

def books(request):
    booklist=book.objects.all()
    return render(request,'book.html',{'book':booklist})

def add(request):
    if request.method=='POST':
        try:
            value=book()
            value.subject = request.POST['subject']
            value.title = request.POST['title']
            value.author = request.POST['author']
            value.publisher = request.POST['publisher']
            value.edition_no = int(request.POST['edition'])
            value.number_of_pages = int(request.POST['number'])
            value.shelf_no = int(request.POST['shelf'])
            value.date = datetime.datetime.now()
            value.save()
            messages.success(request, 'Entered Book Details Has Been Added')
            return redirect('/book')
        except:
            messages.error(request, 'Entered The Valid Information')
            return redirect('/add')
    return render(request,'add.html')

def update(request,id):
    value = book.objects.get(id=id)
    if request.method=='POST':
        try:
            value.subject = request.POST['subject']
            value.title = request.POST['title']
            value.author = request.POST['author']
            value.publisher = request.POST['publisher']
            value.edition_no = int(request.POST['edition'])
            value.number_of_pages = int(request.POST['number'])
            value.shelf_no = int(request.POST['shelf'])
            value.date = datetime.datetime.now()
            value.save()
            messages.success(request, 'Entered Book Details Has Been Updated')
            return redirect('/book')
        except:
            messages.error(request, 'Entered The Valid Information')
            return redirect(f'/update/{id}')
    return render(request,'update.html',{'v':value})

def delete(request,id):
    book.objects.filter(id=id).delete()
    messages.success(request, 'The Book Details Has Been Deleted From The Database')
    return redirect('/book')
