from django.shortcuts import render ,redirect
from .models import List
from .forms import todoform

# Create your views here.
def index(request):

    list = List.objects.all()
    form = todoform() 
    context = {
        'tacks': list,
        'form': form,
            }
    
    if request.method=='POST':
        form = todoform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')



    return render(request,'index.html',context)


def update(request , pk):
    tack = List.objects.get(id=pk)
    form = todoform(instance=tack)
    if request.method == 'POST':        
        form = todoform(request.POST,instance=tack)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'update.html',{'form':form})



def delate(request , pk):
    item = List.objects.get(id=pk)
    if request.method == 'POST':        
        item.delete()
        return redirect('/')

    return render(request,'delate.html',{'item':item})
