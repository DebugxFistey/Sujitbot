from django.urls import path

from bot.views import bot

url_patterns = [
    path('', bot, name='bot'),
]
