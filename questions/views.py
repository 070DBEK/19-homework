from django.shortcuts import render, redirect, get_object_or_404
from .models import Test, Question, Answer
from .forms import TestForm, QuestionFormSet, AnswerFormSet


def test_list(request):
    tests = Test.objects.select_related('lesson').all()
    return render(request, 'questions/test-list.html', {'tests': tests})


def create_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save()
            question_formset = QuestionFormSet(request.POST)
            if question_formset.is_valid():
                for question_form in question_formset:
                    question = question_form.save(commit=False)
                    question.test = test
                    question.save()
                    answer_formset = AnswerFormSet(request.POST)
                    if answer_formset.is_valid():
                        for answer_form in answer_formset:
                            answer = answer_form.save(commit=False)
                            answer.question = question
                            answer.save()
            return redirect('questions:list')

    form = TestForm()
    question_formset = QuestionFormSet(queryset=Question.objects.none())
    answer_formset = AnswerFormSet(queryset=Answer.objects.none())
    return render(request, 'questions/test-formset.html', {'form': form, 'question_formset': question_formset, 'answer_formset': answer_formset})


# def update_test(request, pk):
#     test = get_object_or_404(Test, pk=pk)
#     if request.method == "POST":
#         form = TestForm(request.POST, instance=test)
#         if form.is_valid():
#             form.save()
#             return redirect('questions:list')
#     form = TestForm(instance=test)
#     return render(request, 'questions/test-formset.html', {'form': form})


def update_test(request, pk):
    test = get_object_or_404(Test, pk=pk)

    if request.method == "POST":
        form = TestForm(request.POST, instance=test)
        question_formset = QuestionFormSet(request.POST, queryset=Question.objects.filter(test=test))

        if form.is_valid() and question_formset.is_valid():
            form.save()

            for question_form in question_formset:
                question = question_form.save(commit=False)
                question.test = test  # Test bilan bog‘lash
                question.save()

                # Har bir savol uchun javoblarni olish
                answer_formset = AnswerFormSet(request.POST, queryset=Answer.objects.filter(question=question))
                if answer_formset.is_valid():
                    for answer_form in answer_formset:
                        answer = answer_form.save(commit=False)
                        answer.question = question  # Savol bilan bog‘lash
                        answer.save()

            return redirect('questions:list')

    else:
        form = TestForm(instance=test)
        question_formset = QuestionFormSet(queryset=Question.objects.filter(test=test))

    return render(request, 'questions/test-formset.html', {
        'form': form,
        'question_formset': question_formset
    })


def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    return render(request, 'questions/test-detail.html', {'test': test})


def test_delete(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == 'POST':
        test.delete()
        return redirect('questions:list')
    return render(request, 'questions/test-delete.html', {'test': test})