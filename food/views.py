from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Item
from .forms import ItemForm

# Create your views here.
class IndexView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'items'


class DetailList(DetailView):
    model = Item
    template_name = 'food/view.html'
    

# def detail(request,item_id):
#     item = get_object_or_404(Item,pk=item_id)
    
#     context = {'item':item}
#     return render(request,'food/view.html',context)

class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_price','item_desc','item_image']
    template_name = 'food/add.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
# def create_item(request):
#     form = ItemForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#     return render(request,'food/add.html',{'form':form})

def update_item(request,id):
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