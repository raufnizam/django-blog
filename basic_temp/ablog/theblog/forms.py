from django import forms
from django.contrib.auth import get_user
from .models import Post, Category, Comment


choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag",'header_image', "author",  "category", "body", "snippet")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title here... '}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'name', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list ,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'You Post here...'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            
        }



class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title",  "body", "snippet")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title here... '}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'You Post here...'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'You Snippet here...'}),   
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =  ["body"]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name here...'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your comment here...'}),
        }