
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import BdayForm
from .models import Bday

#Home View for showing the home page of a html document
def homeView(request):
    context={}
    
    return render(request,'home.html',context)


#Birthday form
def addBday(request):
    form=BdayForm()

    if request.method=='POST':
        form=BdayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'bday_form.html',context)

