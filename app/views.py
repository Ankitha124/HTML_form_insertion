from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def first(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('Date is submitted')
    return render(request,'first.html')


def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']

        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Insertion of Topic is Done')
    
    return render(request,'insert_topic.html')

def insert_webpage(request):

    topic=Topic.objects.all()
    d={'topic':topic}
    if request.method=='POST':
        
        topic=request.POST['topic']
        nm=request.POST['nm']
        u=request.POST['u']
        TO=Topic.objects.get(topic_name=topic)
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=nm,url=u)[0]
        WO.save()
        return HttpResponse('Insertion of webpage is done ')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    nm=Webpage.objects.all()
    d={'nm':nm}
    if request.method=='POST':
        nm=request.POST['nm']
        d=request.POST['d']
        author=request.POST['author']
        WO=Webpage.objects.get(name=nm)
        WO.save()
        AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=author)[0]
        AO.save()

        return HttpResponse('insertion of accessrecords is done')
    return render(request,'insert_access.html',d)




def retrieve_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        MSTS=request.POST.getlist('topic')
        print(MSTS)
        RWOS=Webpage.objects.none()

        for i in  MSTS:
            RWOS=RWOS|Webpage.objects.filter(topic_name=i)

        d1={'RWOS':RWOS}
        return render(request,'display_webpage.html',d1)


    return render(request,'retrieve_webpage.html',d)







        


