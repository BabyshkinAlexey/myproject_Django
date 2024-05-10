from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)

def text(title, text):
    return  f'<h2>{title}</h2>' \
            f'<p>{text}</p>'


def main_page(request):
    title = 'Главная страница сайта'
    body_text = '...Текст...'
    logger.info(f'Page "main" is open')
    return HttpResponse(text(title, body_text))


def about_me(request):
    title = 'О себе'
    body_text = '...Информация...<br>'
    logger.info(f'Page "about_me" is open')
    return HttpResponse(text(title, body_text))