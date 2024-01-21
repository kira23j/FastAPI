from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
  return HttpResponse("Hello Django")
def temp_hello(request):
  return render(
    request,"hello.html",{'name':'Django'}
  )

