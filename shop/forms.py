from django import forms
from .models import tickets, Products

class supportForm(forms.ModelForm):
    class Meta:
        model = tickets
        fields = '__all__'
        widgets = {
            'content' : forms.Textarea()
        }
        
class add_product(forms.ModelForm):
    class Meta:
        model = Products
        exclude = ['slug']
        