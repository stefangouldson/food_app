from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator

# Create your views here.

# def index(request):
#     item_list = Item.objects.all()
#     # template = loader.get_template('food/index.html')
#     context = {
#         'item_list': item_list,
#     }
#     return render(request, 'food/index.html', context)

# def details(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item': item,
#     }
#     return render(request, 'food/detail.html', context)


class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('item_name')
        if query:
            object_list = self.model.objects.filter(item_name__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class FoodDetailView(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'

class FoodCreateView(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form':form})

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form':form,'item': item})

def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {'item': item})