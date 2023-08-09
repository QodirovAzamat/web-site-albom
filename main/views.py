from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import  Royxat, Category

def index_page(request):
    royxat = Royxat.objects.all()
    if request.method == 'POST':
        category = request.POST.get('category')
        cat = Category.objects.filter(title=category).first()
        if not cat:
            cat = Category.objects.create(title=category, slug=category)
        task = request.POST.get('task')
        priority = request.POST.get('priority')
        old_task = Royxat.objects.filter(title=task).first()
        if not old_task:
            Royxat.objects.create(title=task, slug=task, category=cat, shirt_size=priority,created=timezone.now())
            return redirect("index")
    return render(request,"main/indext.html",{"royxat":royxat})

def delete_royxat(request,slug):
    royxat = get_object_or_404(Royxat,slug=slug)
    royxat.delete()
    return redirect("index")


