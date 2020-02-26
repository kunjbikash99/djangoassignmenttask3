from django.shortcuts import render,redirect
from myapp.forms import loginform,alreadyf,Blogf
from django.views import generic
from .models import login,already,Blog
from django.http import HttpResponse


# Create your views here.

def log(request):
    if request.method=="POST":
        form=loginform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/sign')
            except:
                pass
    else:
        form=loginform()
        return render(request,'index.html',{'form':form})

def sign(request):
    if request.method=="POST":
        rom=alreadyf(request.POST)
        if rom.is_valid():
            try:
                rom.save()
                return redirect('/blogdisplay')
            except:
                pass
    else:
        rom=alreadyf()
        return render(request,'show.html',{'rom':rom})

#def check(request):
    #ram = login.objects.all()
    #ramu = already.objects.all()
    #if alreadyf.email==loginform.email and alreadyf.password==loginform.password:
 #       return redirect('/blog')
    #else:
     #   return render(request,'failure.html')

def blogs(request):
    if request.method == "POST":
        ram = Blogf(request.POST)
        if ram.is_valid():
            try:
                ram.save()
                return redirect('/blogdisplay')
            except:
                pass
    else:
        ram = Blogf()
        return render(request,'blogsign.html',{'ram':ram})

def blogpage(request):
    emp=Blog.objects.all()
    return render(request,'fetch.html',{'emp':emp})
    #return render(request,'indexblog.html')

def destroy(request,id):
    bik=Blog.objects.get(id=id)
    bik.delete()
    return redirect("/blogpage")

def edit(request,id):
    bik = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'bik': bik})

def update(request,id):
    bik=Blog.objects.get(id=id)
    form=Blogf(request.POST)
    if form.is_valid():
        try:
            form.save()
            return redirect('/blogdisplay')
        except:
            pass
    return render(request, 'edit.html', {'bik': bik})

def blogdisplay(request):
    jha=Blog.objects.all()
    return render(request,'page.html',{'jha':jha})