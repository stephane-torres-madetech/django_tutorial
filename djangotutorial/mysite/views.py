from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    # return HttpResponse("Hello, World")
    return render(request, "polls/home.html", {})