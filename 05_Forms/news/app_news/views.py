from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from .forms import EditNews, AddComment
from .models import NewsItem, Comment
from django.contrib.auth.views import LoginView, LogoutView


class NewsListView(ListView):
    model = NewsItem
    template_name = 'app_news/newsitem_list.html'
    context_object_name = 'newsitems'
    queryset = NewsItem.objects.order_by('-edit_at')[:5]


class NewsDetailView(DetailView):
    model = NewsItem
    template_name = 'app_news/newsitem_detail.html'
    context_object_name = 'newsitem'


class AddNewsView(CreateView):
    model = NewsItem
    template_name = 'app_news/edit_news.html'
    form_class = EditNews
    success_url = '/'


class EditNewsView(UpdateView):
    model = NewsItem
    template_name = 'app_news/edit_news.html'
    form_class = EditNews
    context_object_name = 'comment'
    success_url = '/'


class AddNewsComment(CreateView):
    model = Comment
    template_name = 'app_news/add_comment.html'
    form_class = AddComment

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            save_user = self.request.user
            save_user_name = self.request.user.username
        else:
            save_user = None
            save_user_name = form.cleaned_data['user_name']
        save_comment = Comment(user_name=save_user_name,
                               comment=form.cleaned_data['comment'],
                               news_fk_id=self.kwargs['pk'],
                               user=save_user
                               )
        save_comment.save()
        return HttpResponseRedirect(reverse('NewsDetailView', args=[self.kwargs['pk']]))


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
