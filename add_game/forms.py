from django import forms
from library.models import Post


class DateInput(forms.DateInput):
    input_type = 'date'


class AddGameForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title', 'image', 'description', 'genre',
            'platform', 'release_date', 'slug'
            ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'pad'}),
            'image': forms.FileInput(attrs={'class': 'pad'}),
            'description': forms.Textarea(
                attrs={'class': 'pad', 'cols': 45, 'rows': 5}),
            'genre': forms.Select(choices=Post.GENRES, attrs={'class': 'pad'}),
            'platform': forms.Select(
                choices=Post.GAMING_PLATFORM, attrs={'class': 'pad'}),
            'release_date': DateInput(attrs={'class': 'pad'}),
            'slug': forms.HiddenInput(),
        }
