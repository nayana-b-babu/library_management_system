from.models import returnbook,purchasebook
from django import forms
class BookingForm(forms.ModelForm):
    class Meta:
        model = returnbook
        fields = ['stud_name','book_name','return_date']
        labels ={
               'stud_name': 'Student Name',
               'book_name' : 'Select the Book',
               'return_date' : 'Return Date'
        }
        widgets = {
            'stud_name' : forms.TextInput(attrs = {'placeholder':'Enter your Name','class':'form-control'}),
            'book_name' : forms.Select(attrs = {'class':'form-control'}),
            'return_date' : forms.DateInput(attrs = {'type':'date','class':'form-control'})
        }

class PurchaseBookForm(forms.ModelForm):
    class Meta:
        model = purchasebook
        fields = ['stud_name','book_name']
        labels = {
                 'stud_name': 'Student Name',
                 'book_name' : 'Book Name',
        }
        widgets = {
            'stud_name': forms.TextInput(attrs = {'placeholder':'Enter your Name','class':'form-control'}),
            'book_name': forms.Select(attrs = {'class':'form-control'}),
        }