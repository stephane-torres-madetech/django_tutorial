from django.http import HttpResponse
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
    return HttpResponse("You're looking at question %s." % question_id)

def vote(request, question_id: int):
    return HttpResponse(f"You're voting for question: {question_id}")
