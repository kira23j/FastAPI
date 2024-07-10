from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
# Create your views here.


def say_hello(request):
    product=Product.objects.all()
    return render(request,'hello.html',{'name':'kira23j'})
