from django.db.models import TextField
from django.forms import TextInput, ModelForm, DateInput, forms, Form, IntegerField

from .models import Comments


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text', )
        widgets = {
            'text': TextInput(
                attrs={
                    'placeholder': 'Your comment'
                }
            ),
        }

