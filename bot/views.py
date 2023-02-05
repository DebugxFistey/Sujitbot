from django.shortcuts import render
import openai
from django.http import JsonResponse
import wikipedia



# Create your views here.

def bot(request):
    return render(request,"index.html")

def get_data(request):
    msgerInput = request.GET.get("msgerInput")
    selectInput = request.GET.get("selectInput")
    print(selectInput)
    if selectInput == 'openai':
        message = chat_bot(request, msgerInput)
    elif selectInput == 'image':
        message = image_generate(request, msgerInput)

    print(message)
    result = {
        'data': message
    }

    return JsonResponse(result)


def chat_bot(request, msgerInput):
    openai.api_key = "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"
    completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=msgerInput,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
    message = completions.choices[0].text
    return message

def image_generate(request, msgerInput):
    openai.api_key = "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"
    response = openai.Image.create(
        prompt=msgerInput,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    img_src = f"<img src={image_url} width='200px' height='200px'>"
    return img_src
