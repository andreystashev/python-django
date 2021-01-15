from random import randint
import datetime
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from .models import Advertisement
from .forms import CountForm


class MainView(View):
    def get(self, request):
        advertisements = Advertisement.objects.all()[:3]
        content = {'advertisements': advertisements}
        return render(request, 'advertisements_app/main.html', content)


class RandomView(View):
    def get(self, request):
        count = Advertisement.objects.count()
        random_object = Advertisement.objects.all()[randint(0, count - 1)]
        content = {'advertisements': random_object}
        return render(request, 'advertisements_app/random.html', content)


class AdsListView(ListView):
    model = Advertisement
    template_name = 'advertisements.html'
    context_object_name = 'advertisements'
    queryset = Advertisement.objects.all()[:5]


class AdsDetailView(DetailView):
    model = Advertisement


class FillDB(View):
    def get(self, request, *args, **kwargs):
        count_form = CountForm()
        content = {'message': '',
                   'count_form': count_form}
        return render(request, 'advertisements_app/fill_db.html', content)

    def post(self, request, *args, **kwargs):
        count_form = CountForm(request.POST)
        content = {}
        if count_form.is_valid():
            count = count_form.cleaned_data['counter']
            for i in range(0, count):
                new_advertisement = Advertisement(title='Объявление ' + str(i),
                                                  description='Текст объявления' + str(i),
                                                  price=i,
                                                  created_at=datetime.datetime.now(),
                                                  finish_at=datetime.datetime.now() + datetime.timedelta(weeks=5),
                                                  views_count=i
                                                  )
                new_advertisement.save()
            content = {'message': 'Записи добавалены',
                       'count_form': count_form}
        return render(request, 'advertisements_app/fill_db.html', content)
