from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def tester(request):
    return HttpResponse("Testing out adding new route to a urls file")
