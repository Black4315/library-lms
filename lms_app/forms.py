from django import forms
from .models import Book,category


class Addcat(forms.ModelForm):
     class Meta:
          model = category
          fields = ['name']
          widgets = {
               'name':forms.TextInput(attrs={'class':'form-control'}),
               }
class Addbook(forms.ModelForm):
     class Meta:
          model = Book
          fields='__all__'     
               
          widgets = {
               
               'title':forms.TextInput(attrs={'class':'form-control'}),
               'author':forms.TextInput(attrs={'class':'form-control'}),
               'author_photo':forms.FileInput(attrs={'class':'form-control'}),
               'book_photo':forms.FileInput(attrs={'class':'form-control'}),
               'pages':forms.NumberInput(attrs={'class':'form-control'}),
               'price':forms.NumberInput(attrs={'class':'form-control'}),
               'rental_price_day':forms.NumberInput(attrs={'class':'form-control','id':'rentalDay'}),
               'rental_period':forms.NumberInput(attrs={'class':'form-control','id':'rentalper'}),
               'totalrental':forms.NumberInput(attrs={'class':'form-control','id':'totalrental'}),
               'state_book':forms.Select(attrs={'class':'form-control'}),
               'category':forms.Select(attrs={'class':'form-control'}),
          
           }
               
          
        
          