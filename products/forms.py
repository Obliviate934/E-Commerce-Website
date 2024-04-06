# books/forms.py
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
import re
from django.core.exceptions import ValidationError
from datetime import date

def validate_name(value):
    pattern = r'^[a-zA-Z ]{2,20}$'
    if not re.match(pattern, value):
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)
    
def validate_email(value):
    pattern = r'^[\w\.]+@[\w\.]+\.\w+$'
    if not re.match(pattern, value):
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)
    
def validate_description(value):
    pattern = r'^(.|\s)+[\w\.]+(.|\s)$'
    if not re.match(pattern, value):
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, validators=[validate_name])
    email = forms.EmailField(validators=[validate_email])
    subject = forms.CharField(max_length=200, validators=[validate_description])
    message = forms.CharField(widget=forms.Textarea, validators=[validate_description])

class CheckoutForm(forms.Form):
    card_number = forms.CharField(label='Card Number', max_length=16)
    expiry_date = forms.CharField(label='Expiry Date', max_length=7)
    cvv = forms.CharField(label='CVV', max_length=4)

# class ExpiryDateField(forms.CharField):
#     def validate(self, value):
#         super().validate(value)
#         if not re.match(r'^\d{2}/\d{4}$', value):
#             raise ValidationError('Invalid expiry date format. Please use MM/YYYY.')
        
#         # Split the input to get month and year
#         month, year = map(int, value.split('/'))
        
#         # Validate month (should be between 1 and 12)
#         if month < 1 or month > 12:
#             raise ValidationError('Invalid month. Please enter a value between 1 and 12.')
        
#         # Validate year (should not be in the past or after 2024)
#         if year < date.today().year or year > 2024:
#             raise ValidationError('Invalid year. Please enter a value between {} and 2024.'.format(date.today().year))
        
# class CheckoutForm(forms.Form):
#     card_number = forms.CharField(label='Card Number', max_length=16)
#     expiry_date = ExpiryDateField(label='Expiry Date', max_length=7)
#     cvv = forms.CharField(label='CVV', max_length=3)

#     def clean(self):
#         cleaned_data = super().clean()
#         print("Cleaned data:", cleaned_data)
#         return cleaned_data

#     def clean_card_number(self):
#         card_number = self.cleaned_data['card_number']
#         if not re.match(r'^\d{16}$', card_number):
#             raise ValidationError('Invalid card number')
#         return card_number

#     def clean_cvv(self):
#         cvv = self.cleaned_data['cvv']
#         if not re.match(r'^\d{3,4}$', cvv):
#             raise ValidationError('Invalid CVV')
#         return cvv

    
class CustomPasswordChangeForm(PasswordChangeForm):
    # Add any customizations if needed
    pass
