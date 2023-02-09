from django.shortcuts import render
from django.http import JsonResponse
import wikipediaapi
import requests



# Create your views here.

def bot(request):
    return render(request,"index.html")

def get_data(request):
    msgerInput = request.GET.get("msgerInput")
    selectInput = request.GET.get("selectInput")
    print(selectInput)
    if selectInput == 'bot':
        message = chat_bot(request, msgerInput)
    elif selectInput == 'wikipedia':
        message = wikipedia(request, msgerInput)

    print(message)
    result = {
        'data': message
    }

    return JsonResponse(result)


def chat_bot(request, msgerInput):
    url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"

    payload = {
        "enable_google_results": "true",
        "enable_memory": False,
        "input_text": "messi"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": "6fa7b260-0e4c-4890-b8a4-3fc5ec6e01e7"
    }

    response = requests.post(url, json=payload, headers=headers).json()["message"]
    return response

def wikipedia(request, msgerInput):

    wiki_wiki = wikipediaapi.Wikipedia('en')

    page_py = wiki_wiki.page(msgerInput)
    response = page_py.summary
    return response
