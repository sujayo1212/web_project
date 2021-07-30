from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Lecture
from .forms import LectureForm


class LectureList(ListView):
    model = Lecture


class LectureDetail(DetailView):
    model = Lecture


def lecture_create(request):
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.save()
            return redirect('lecture:index')
    else:
        form = LectureForm()
    context = {'form': form}
    return render(request, 'lecture/lecture_create.html', context)


def lecture_update(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.method == "POST":
        form = LectureForm(request.POST, request.FILES, instance=lecture)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.save()
            return redirect('lecture:detail', pk=lecture_id)
    else:
        form = LectureForm(instance=lecture)
    context = {'form': form}
    return render(request, 'lecture/lecture_update.html', context)


def lecture_delete(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    lecture.delete()
    return redirect('lecture:index')
