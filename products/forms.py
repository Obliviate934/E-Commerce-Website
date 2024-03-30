# books/forms.py
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
import re
from django.core.exceptions import ValidationError

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

class CustomPasswordChangeForm(PasswordChangeForm):
    # Add any customizations if needed
    pass