from django import forms
from django.forms import widgets


class GuestForm(forms.Form):
    guest_name = forms.CharField(max_length=40, required=True, label="Guest name:")
    guest_mail = forms.CharField(max_length=254, required=True, label="Guest e-mail:")
    guest_text = forms.CharField(max_length=2000, required=True, label="Guest note:",
                                 widget=widgets.Textarea(attrs={"rows": 7, "cols": 50}))
