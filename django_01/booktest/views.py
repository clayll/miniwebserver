from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from booktest.models import *

# Create your views here.
def index(request):
    list = BookInfo.objects.all()
    content = {"title":"图书管理","list":list}
    return render(request,'booktest/index.html',content)

def detail(request, bid):
    book = BookInfo.objects.get(id = int(bid))
    heros = book.heroinfo_set.all()

    return render(request,'booktest/detail.html',{'book': book,'heros': heros})

def create(request):
    newBook = BookInfo()
    newBook.btitle = "流星蝴蝶剑"
    newBook.bpub_date = datetime.date(1995,12,30)
    newBook.save()
    # return HttpResponse("ok")
    return redirect('/index')

def delete(request, bid):
    book = BookInfo.objects.get(id=int(bid))
    book.delete()
    return redirect('/index')