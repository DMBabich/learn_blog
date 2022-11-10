from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    name = forms.CharField(label='Name',
                           widget=forms.TextInput(
                               attrs={'placeholder':'Name', 'class':'form-control'}
                           ))
    text = forms.CharField(label='Text',
                           widget=forms.Textarea(
                               attrs={'placeholder':'Text', 'class':'form-control'}
                           ))

    class Meta:
        model = Post
        fields = '__all__'