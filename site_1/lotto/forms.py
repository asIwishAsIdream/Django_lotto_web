from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):
    
    # 상위의 라는 뜻
    class Meta:
        model = GuessNumbers
        fields = ('name', 'text','test')