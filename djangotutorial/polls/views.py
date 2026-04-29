from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Question


def index(request):
    latest_questions = Question.objects.order_by("-date_published")[:5]
    context = {"latest_questions": latest_questions}
    return render(request, "polls/questions.html", context)

def tester(request):
    return HttpResponse("Testing out adding new route to a urls file")

def results(request, question_id: int):
    response = f"You're looking the results for question: {question_id}"
    return HttpResponse(response)

def detail(request, question_id: int):
    # we can use Question.get_object_or_404 to replace the try except block,
    # prefer the blocks as can handle different errors and do a conditional template render
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/details.html", {"question":question})


def vote(request, question_id: int):
    return HttpResponse(f"You're voting for question: {question_id}")
