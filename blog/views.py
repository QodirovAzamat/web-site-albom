from django.shortcuts import render ,redirect
from .models import  Post
from django.views import View
from django.views.generic import CreateView
from .forms import PostForm

def kun_uz(request):
    post = Post.objects.all()
    return render(request,"main/kun.html",{"post":post})

   
class PostCreate(View):
    def get(self,request):
        form = PostForm()
        return render(request,"post/add.html",{"form":form})
    
    def post(self,request):
        form = PostForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("post-create")
        return render(request,"post/add.html",{"form":form})
