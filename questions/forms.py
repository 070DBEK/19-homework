from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from lessons.models import Lesson
from .models import Test, Question, Answer


class TestForm(forms.ModelForm):
    lesson = forms.ModelChoiceField(
        queryset=Lesson.objects.all(),
        widget=forms.Select(attrs={
            'class': 'w-full border border-gray-300 rounded p-2'
        }),
        error_messages={
            'required': "Iltimos, darsni tanlang."
        }
    )

    class Meta:
        model = Test
        fields = ['name', 'lesson']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded p-2'
            }),
        }
        error_messages = {
            'name': {
                'required': "Test nomini kiriting.",
                'max_length': "Test nomi juda uzun. Kamroq harflar ishlating."
            }
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise ValidationError("Test nomi kamida 3 ta harfdan iborat bo‘lishi kerak.")
        return name


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded p-2'
            }),
        }
        error_messages = {
            'text': {
                'required': "Savol matnini kiriting.",
                'max_length': "Savol matni juda uzun. Kamroq so‘z ishlating."
            }
        }

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 5:
            raise ValidationError("Savol matni kamida 5 ta belgidan iborat bo‘lishi kerak.")
        return text


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded p-2'
            }),
        }
        error_messages = {
            'text': {
                'required': "Javob matnini kiriting.",
                'max_length': "Javob matni juda uzun. Kamroq so‘z ishlating."
            },
            'is_correct': {
                'required': "Iltimos, bu javob to‘g‘ri yoki noto‘g‘ri ekanligini belgilang."
            }
        }

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 2:
            raise ValidationError("Javob matni kamida 2 ta belgidan iborat bo‘lishi kerak.")
        return text

    def clean_is_correct(self):
        is_correct = self.cleaned_data.get('is_correct')
        if is_correct not in [True, False]:
            raise ValidationError("Iltimos, javobning to‘g‘riligini aniqlang.")
        return is_correct


AnswerFormSet = inlineformset_factory(
    Question, Answer,
    form=AnswerForm,
    extra=2,
    can_delete=True
)


QuestionFormSet = inlineformset_factory(
    Test, Question,
    form=QuestionForm,
    extra=0,
    can_delete=True
)
