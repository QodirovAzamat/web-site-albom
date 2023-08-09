from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        fields = ('title','slug','category','description','author','published','image','publish_date','tag')
        model = Post