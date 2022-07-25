from django.shortcuts import render
from . models import Information
from . forms import InfoModelForm
# Create your views here.

def create(request):
    if request.method == "POST":
        frm = InfoModelForm(request.POST)
        if frm.is_valid():
            frm.save()
            frm = InfoModelForm()
    else :
        frm = InfoModelForm()
        data = Information.objects.all()
    return render(request ,'logic.html',{"form" : frm } )

def read(request):
    read = Information.objects.all()
    return render (request,'logic.html',{'data': read})

def update(request, pk):
    var = Information.objects.get(id = pk)
    frm = InfoModelForm(request.POST or None, instance = var)
    if frm.is_valid():
        frm.save()
        frm = InfoModelForm()
    data = Information.objects.all()
    return render (request, 'change.html' , {"form" : frm  , "data" : data})

def delete (request , id):
    var = Information.objects.get(id = id)
    frm = InfoModelForm(request.POST or None, instance = var)
    if frm.is_valid():
       var.delete()
       frm = InfoModelForm()
    data = Information.objects.all()
    return render(request, 'delete.html' , {"form" : frm , "data" : data}) 