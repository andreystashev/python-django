from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .forms import ChoiceForm, AdvertisementForm
from .settings import SERVICE_ADVERTISEMENTS, CAR_ADVERTISEMENTS, ELECTRONIC_ADVERTISEMENTS, CATEGORIES_LIST, \
    REGION_LIST


class Count:
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        return self.counter


count = Count()


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Объявления в вашем городе'
        context['title'] = 'Бесплатные объявления'
        context['description'] = """
        Вашему вниманию предлагается лучший сайт объявлений вашего города. Здесь вы найдете всё, что вам нужно! 
        И даже больше!
        """
        return context


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone'] = '8-800-555-35-35'
        context['email'] = 'bestadvertising@ya.ru'
        context['address1'] = 'МО, г Раменское, ул Сосновый бор, д.4 , 140100'
        context['address2'] = 'МО, г Воскресенск, ул Молодежная, д.10 , 146134'
        return context


def categories(request, *args, **kwargs):
    return render(request, 'advertisements/categories.html', {'categories_list': CATEGORIES_LIST})


class Regions(View):
    def get(self, request):
        return render(request, 'advertisements/regions.html', {'region_list': REGION_LIST})

    def post(self, request):
        regions_list = ['Регион успешно создан']
        return render(request, 'advertisements/regions.html', {'region_list': regions_list})


class IndexPage(View):
    def get(self, request):
        choice_form = ChoiceForm()
        choice_message = ''
        context = {'choice_form': choice_form, 'choice_message': choice_message}
        return render(request, 'advertisements/index.html', context)

    def post(self, request):
        choice_form = ChoiceForm(request.POST)
        choice_message = ''
        post_count = next(count)
        if choice_form.is_valid():
            choice_message = 'Данные успешно выбраны'
        context = {'choice_form': choice_form, 'choice_message': choice_message, 'post_count': post_count}
        return render(request, 'advertisements/index.html', context)


class Advertisements(View):
    def get(self, request):
        context = {'service_advertisements': SERVICE_ADVERTISEMENTS,
                   'car_advertisements': CAR_ADVERTISEMENTS,
                   'electronic_advertisements': ELECTRONIC_ADVERTISEMENTS}
        return render(request, 'advertisements/advertisements.html', context)

    def post(self, request):
        post_form = AdvertisementForm()
        message = ['запрос на создание новой записи успешно выполнен']
        context = {'service_advertisements': SERVICE_ADVERTISEMENTS,
                   'car_advertisements': CAR_ADVERTISEMENTS,
                   'electronic_advertisements': ELECTRONIC_ADVERTISEMENTS,
                   'message': message
                   }
        return render(request, 'advertisements/advertisements.html', context)


