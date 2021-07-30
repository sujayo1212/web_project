from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
#from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Q&A 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, './qna/question_list.html', context)

def detail(request, question_id):
    """
    Q&A 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, './qna/question_detail.html', context)

def answer_create(request, question_id):
    """
    Q&A 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('qna:detail', question_id=question.id)
# render, redirect 개념 정리 answer_create같은 경우 url이 아닌 int:question이라 다르게 연결 (urls.py참조)