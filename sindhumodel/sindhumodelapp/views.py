from django.shortcuts import render
from sindhumodelapp import  forms
from sindhumodelapp.models import Worldcup

# Create your views here.
def Worldcupmain(request):
    return render(request,'modelapp/main.html')
def add(request):
    form=forms.Worldcupform()
    if request.method=='POST':
        form=forms.Worldcupform(request.POST)
        if form.is_valid():
           form.save(commit=True)
        return Worldcupmain(request)
    return render(request,'modelapp/add.html',{'form':form})
def model(request):
    match_list=Worldcup.objects.all()
    return render(request,'modelapp/model.html',{'match_list':match_list})
