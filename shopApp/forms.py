from django import forms
from shopApp.models import Contact

class formComment(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)

class formContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'address', 'phone', 'email']
