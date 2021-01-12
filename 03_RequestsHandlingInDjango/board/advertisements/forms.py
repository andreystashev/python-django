from django import forms


class ChoiceForm(forms.Form):
    region = forms.ChoiceField(choices=(
        (1, 'Кемеровская область'), (2, 'Московская область'), (3, 'Дагестан'), (4, 'Хакасия')))
    category = forms.ChoiceField(choices=((1, 'Сервис'), (2, 'Авто'), (3, 'Электроника')))
    topic = forms.CharField()


class AdvertisementForm(forms.Form):
    counter = forms.IntegerField(disabled=True, initial=0)
