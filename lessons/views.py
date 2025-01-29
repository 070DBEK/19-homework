from django.shortcuts import render, get_object_or_404, redirect
from .models import Lesson
from questions.models import Test
from .forms import LessonForm


def home(request):
    test = Test.objects.first()
    return render(request, 'index.html', {'test': test})


def lessons_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lesson-list.html', {'lessons': lessons})


def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    tests = Test.objects.filter(lesson=lesson)
    return render(request, 'lessons/lesson-detail.html', {
        'lesson': lesson,
        'tests': tests,
    })


def create_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lessons:list')
    else:
        form = LessonForm()
    return render(request, 'lessons/lesson-create.html', {'form': form})


def update_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lessons:list')
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'lessons/lesson-create.html', {'form': form, 'lesson': lesson})


def lesson_delete(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    tests = Test.objects.filter(lesson=lesson)
    if request.method == 'POST':
        tests.delete()
        lesson.delete()
        return redirect('lessons:list')
    return render(request, 'lessons/lesson-delete.html', {'lesson': lesson, 'tests': tests})