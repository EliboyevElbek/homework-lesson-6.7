from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def HomeView(request):
    txt = "<h1>Bosh sahifa</h1> <p><a href=about/>Aboutga o'tish</a></p>"
    return HttpResponse(txt)

def AboutView(request):
    txt = ("<h1>About sahifa</h1> <p><a href=/>Bosh sahifaga qaytish</a></p> "
           "<p><a href=/pay/>To'lov bo'limiga o'tish</a></p>")
    return HttpResponse(txt)

def PayView(request):
    txt = ("<h1>To'lov bo'limi</h1> <p><a href=/about/>Aboutga qaytish</a></p> "
           "<p><a href=/product/>Maxsulotlar haqida batafsil...</a></p>")
    return HttpResponse(txt)

def ProductView(request):
    txt = ("<h1>Maxsulotlar bo'limi</h1> <p><a href=/pay/>To'lov bo'limiga qaytish</a></p> "
           "<p><a href=/contact/>Biz bilan bo'lanish</a></p>")
    return HttpResponse(txt)

def ContactView(request):
    txt = ("<h1>Biz bilan bog'lanish</h1> <p><a href=/product/>Maxsulotlar bo'limiga qaytish</a></p> "
           "<p><a href=/>Bosh sahifaga qaytish</a></p>")
    return HttpResponse(txt)