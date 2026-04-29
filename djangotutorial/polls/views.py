from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def tester(request):
    return HttpResponse("Testing out adding new route to a urls file")

def results(request, question_id: int):
    response = f"You're looking the results for question: {question_id}"
    return HttpResponse(response)

def detail(request, question_id: int):
    return HttpResponse("You're looking at question %s." % question_id)

def vote(request, question_id: int):
    return HttpResponse(f"You're voting for question: {question_id}")
