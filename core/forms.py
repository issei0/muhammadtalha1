# from django import forms
from django.forms import ModelForm
from .models import Contact
# Create your forms here.
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

# class ContactForm(forms.Form):
# 	full_name = forms.CharField(label="Name", max_length=50)
# 	sender = forms.EmailField(label="Email", max_length=150)
# 	message = forms.CharField(label="Message", widget=forms.Textarea, max_length = 2000)