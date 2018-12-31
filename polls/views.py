from django.http import Http404
from django.shortcuts import render

from .models import Question


# Create your views here.
def index(request):
    listeQuestions = Question.objects.order_by('-datePublication')[:5]
    context = {'listeQuestions': listeQuestions}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("La question %s n'existe pas" % question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)