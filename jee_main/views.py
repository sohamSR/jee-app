from django.shortcuts import render
from django.http import HttpResponse
from .forms import MCQFORM, NUMERICALFORM

# Create your views here.
def index(request):
    form1=MCQFORM()
    if request.method == 'POST':
        print(request.POST)
        form1=MCQFORM(request.POST)
        if form1.is_valid():
            form1.save()
            form1 = MCQFORM()
    
    context = {'form1': form1}
    return render(request, 'index.html', context)

def numerical(request):
    form2=NUMERICALFORM()
    if request.method == 'POST':
        print(request.POST)
        form2=NUMERICALFORM(request.POST)
        if form2.is_valid():
            form2.save()
            form2=NUMERICALFORM()
    
    context = {'form2':form2}
    return render(request, 'numerical.html', context)