from django import forms
from library.models import Post


class AddGameForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'image', 'description', 'genre', 'platform', 'release_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'pad'}),
            'image': forms.FileInput(attrs={'class': 'pad'}),
            'description': forms.Textarea(attrs={'class': 'pad', 'cols': 60, 'rows': 5}),
            'genre': forms.Select(choices=Post.GENRES, attrs={'class': 'pad'}),
            'platform': forms.Select(choices=Post.GAMING_PLATFORM, attrs={'class': 'pad'}),
            'release_date': forms.DateInput(attrs={'class': 'pad'})
        }
