from django.http import HttpRequest,HttpResponse
from django.shortcuts import render , redirect
from .forms import *
from .models import *


def post_list_view(request):
    posts = Expense.objects.all()
    return render(request,'posts-list.html',{"posts":posts})

def create_list_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('posts-list')
    else:
        form = PostForm()
        return render(request,'post-form.html',{"form":form})
    
def edit_list_view(request,pk):
    post = Expense.objects.filter(id=pk).first()
    if post:
        if request.method == "POST":
            form = PostForm(request.POST,instance=post)
            if form.is_valid():
                form.save()
                return redirect("posts-list")
        else:
            form = PostForm(instance=post)
        return render(request,"post-form.html",{"form":form})
    else: 
        return HttpResponse("Post is not found!")
        

def delete_list_view(request,pk):
    post = Expense.objects.filter(id=pk).first()
    if post:
        if request.method == "POST":
            post.delete()
            return redirect("posts-list")
        else:
            return render(request,"confirmationpostdelete.html",{"post":post})
