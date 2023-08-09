from django.urls import path
from .views import index_page,delete_royxat
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('',index_page,name="index"),
    path('delete/<slug:slug>', delete_royxat,name="delete_royxat"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
