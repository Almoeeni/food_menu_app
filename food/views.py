from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from django.template import loader
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    item = Item.objects.all()
    context = {'items':item}
    return render(request, 'food/index.html',context)

def detail(request,item_id):
    item = get_object_or_404(Item,pk=item_id)
    
    context = {'item':item}
    return render(request,'food/view.html',context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/add.html',{'form':form})

def update_item(request,id):
    print(id)
    item = get_object_or_404(Item,pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form, 'item':item})

def delete_item(request,id):
    item = get_object_or_404(Item,pk=id)
    
    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item})