from asyncio.windows_events import NULL
from operator import contains
from re import X
from turtle import title
from django.shortcuts import render
from .models import Lawyer,Tag
# Create your views here.
def projects(request):
    projects=Lawyer.objects.all()
    tags=Tag.objects.all()
    context={'projects':projects,'tags':tags}
     
    
    return render(request,'lawyers.html',context);

def talklawyer(request):
    projects=Lawyer.objects.all()
    tags=Tag.objects.all()
    context={'projects':projects,'tags':tags}
    return render(request,'askaquestion.html',context)

def askaquestion(request):
    projects=Lawyer.objects.all()
    tags=Tag.objects.all()
    context={'projects':projects,'tags':tags}
    return render(request,'blank.html',context)


def test(request):
    if request.method == "POST" :
        x = request.POST['city']
        y = request.POST['tag']
    item=Lawyer.objects.filter(location=x , practice_area__name=y)
    context={'lawyers':item,'x':x,'y':y}
    return render(request,'hello-world.html',context)

def project(request,pk):
    projectObj=Lawyer.objects.get(id=pk)
    return  render(request,'singlelawyer.html',{'lawyer':projectObj,})

def aboutus(request):
    return  render(request,'aboutus.html')

def search(request):
    if request.method == "POST" :
        x = request.POST['search']
    from django.core.exceptions import ObjectDoesNotExist
    data=NULL
    datatype=NULL
    temp=NULL
    try:
        data=Lawyer.objects.get(title__contains=x)
        datatype="name"
    except ObjectDoesNotExist:
        print("error")
        
        temp=1
        try:
            data=Lawyer.objects.filter(practice_area__name__contains=x)
            datatype="practice_area"
        except ObjectDoesNotExist:
            print("sad")
    if temp==1:
        if data.count() == 0:        
            print("asd")
            try:
                data=Lawyer.objects.filter(location__contains=x)
                datatype="location"
            except ObjectDoesNotExist:
                data=NULL
                datatype="nulltype"
    
    print(data)
    context={'data':data,'datatype':datatype,'x':x,'a':"name",'b':"practice_area",'c':"location"}
    return render(request,'search_lawyers.html',context)