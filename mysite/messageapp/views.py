from django.shortcuts import render

from django.http import JsonResponse

# Create your views here.

data = {
    "Name": "Eyerusalem",
    "Track": "Backend(Python)",
    "Message": "Hi, Mentor, you're doing a great job!"
}

def index(request):
    return JsonResponse(data)

    