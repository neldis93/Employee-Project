from django import forms
from .models import Test

class TestForm(forms.ModelForm):   

    class Meta:
        model = Test
        fields = ('title','subtitle', 'quantity',)

        #Personalizar el formulario
        widgets= { 'title': forms.TextInput(
            attrs= { 
                'placeholder': 'Enter text here'
            }
        )

        }

    def clean_quantity(self):
        quantity= self.cleaned_data['quantity'] # con esto le digo que recupere el valor quantity 
        if quantity < 10:
            raise forms.ValidationError('Enter a new one greater than 10')
        return quantity