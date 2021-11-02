
from django import forms
from blog.models import Dog, Activity, Breed, Comment

class DateInput(forms.DateInput):
    input_type = 'date'
class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('name', 'weight', 'date_of_birth', 'image','description', 'owner', 'breed')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'weight': forms.NumberInput(attrs={'class':'form-control'}),
            'date_of_birth': DateInput(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'owner': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'input', 'type':'hidden'}),
            'breed': forms.Select(attrs={'class': 'form-control'}),
        }
class UpdateDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('weight', 'image', 'description', 'breed')
        widgets = {
            'weight': forms.NumberInput(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'breed': forms.Select(attrs={'class': 'form-control'}),
        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'date', 'description', 'location', 'owner')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'date': DateInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'location': forms.Textarea(attrs={'class':'form-control'}),
            'owner': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'input', 'type':'hidden'}),
        }
class UpdateActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('date', 'description', 'location')
        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'location': forms.Textarea(attrs={'class':'form-control'}),
        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'input', 'type':'hidden'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }
class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'input', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }