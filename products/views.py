from django.shortcuts import render
from django.views import View
from products.models import Categories,Products
from django.core.paginator import Paginator


# Create your views here.

class CategoriesView(View):
    def get(self,request):
        categories=Categories.objects.all()
        pagination=Paginator(categories,3)
        page=request.GET.get('page',1)
        pages=pagination.get_page(page)
        context={
            'pages':pages
        }
        return render(request,'categories.html',context)

    def post(self,request):
        if request.method == "POST":
            search = request.POST['search']
            datas=Products.objects.filter(title__icontains=search)
            pages = Categories.objects.filter(title__icontains=search)
            return render(request, 'categories.html', {'pages': pages,'datas':datas})

        return render(request,'categories.html')

class ProductsView(View):
    def get(self,request,id):
        categories = Categories.objects.all()
        products = Products.objects.filter(categories=id)
        pagination = Paginator(products, 3)
        page = request.GET.get('page',1)
        pages = pagination.get_page(page)
        context = {
            'pages': pages,
            'categories':categories
        }
        return render(request,'index.html',context)

    def post(self,request):
        if request.method == "POST":
            search = request.POST['search']
            datas=Products.objects.filter(title__icontains=search)
            pages = Categories.objects.filter(title__icontains=search)
            return render(request, 'categories.html', {'pages': pages,'datas':datas})

        return render(request,'categories.html')



class DetailView(View):
    def get(self,request,id):
        products = Products.objects.filter(id=id)
        categories = Categories.objects.all()
        context = {
            'products': products,
            'categories': categories
        }
        return render(request, 'detail.html', context)




