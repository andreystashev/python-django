from django import forms


from .models import NewsItem, Comment


class AddNews(forms.ModelForm):
    class Meta:
        model = NewsItem
        fields = '__all__'


class EditNews(forms.ModelForm):
    class Meta:
        model = NewsItem
        fields = '__all__'


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'user_name']
        widgets = {
            'comment': forms.Textarea(attrs={'label': 'Комментарий '}),
            'user_name': forms.TextInput(attrs={'label': 'Имя пользователя '}),
        }

class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)