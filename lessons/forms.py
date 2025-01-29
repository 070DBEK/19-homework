from django import forms
from .models import Lesson


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'desc']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) <= 2:
            raise forms.ValidationError('Name must be at least 1 characters long.')
        return name