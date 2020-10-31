from django.http import HttpResponse

from django.views import View
import random


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        self.list = ['<li>Установить python</li> ',
                     '<li>Установить django</li> ',
                     '<li>Запустить сервер</li> ',
                     '<li>Порадоваться результату</li> ',
                     '<li>Привет мир!</li> ']
        random.shuffle(self.list)
        self.randomlist = ''.join(self.list)
        return HttpResponse('<ul> ' + self.randomlist +
                            ' </ul>')
