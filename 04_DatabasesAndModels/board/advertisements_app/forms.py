from django import forms


class CountForm(forms.Form):
    counter = forms.IntegerField(initial=0, max_value=1000)
