from django import forms
from .models import Lesson


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'desc']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded p-2',
                'placeholder': 'Enter lesson name'
            }),
            'desc': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded p-2',
                'rows': 3,
                'placeholder': 'Enter lesson description'
            }),
        }
        error_messages = {
            'name': {
                'required': "Lesson nomini kiriting.",
                'max_length': "Lesson nomi juda uzun. Kamroq harflar ishlating."
            },
            'desc': {
                'required': "Dars tavsifini kiriting.",
            }
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('Lesson name must be at least 3 characters long.')
        return name

    def clean_desc(self):
        desc = self.cleaned_data.get('desc')
        if not desc:
            raise forms.ValidationError("Lesson description cannot be empty.")
        return desc