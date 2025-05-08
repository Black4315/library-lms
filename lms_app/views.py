from django.shortcuts import render,redirect
from .models import *
from .forms import Addcat,Addbook



def index(req):
    context={
        "categorys":category.objects.all(),
        "books":Book.objects.all(),
        "addbook":Addbook(),
        "addcat":Addcat(),
        "allbooks":Book.objects.all().count(),
        "booksAva":Book.objects.filter(state_book='Available').count(),
        "booksSol":Book.objects.filter(state_book='sold').count(),
        "booksRen":Book.objects.filter(state_book='rental').count(),
    }
    
    if req.method == 'POST':
        data = Addbook(req.POST,req.FILES)
        print(req.POST,'\n','\n',req.FILES)
        if data.is_valid():
            data.save()

        datacat = Addcat(req.POST)
        if datacat.is_valid():
            datacat.save()    
   
    return render(req,'pages/index.html',context)

def books(req):
    title = None
    search = Book.objects.all()
    
    if 'search_name' in req.GET:
        title =req.GET['search_name']
        if title:
            search = search.filter(state_book__contains = title)
  
    context={"books":search,}
    return render(req,'pages/books.html',context)

def update(req,id):
    book_id= Book.objects.get(id=id)
    if req.method == 'POST':
        bookSave = Addbook(req.POST,req.FILES,instance=book_id)
        if bookSave.is_valid():
            bookSave.save()  
            return redirect('/') 

    else:
        bookSave = Addbook(instance=book_id)
    cont={"form":bookSave}
   
    return render(req,'pages/update.html',cont)

def delete(req,id):
     context={"addbook":Addbook(),}
     book_id= Book.objects.get(id=id)
     if req.method == 'POST':
        book_id.delete()
        return redirect('/')
     return render(req,'pages/delete.html',context)
# Create your views here.
