from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view()),
    path('newsitems', views.NewsListView.as_view(), name='NewsListView'),
    path('newsitems/<int:pk>', views.NewsDetailView.as_view(), name='NewsDetailView'),
    path('edit_news/', views.AddNewsView.as_view(), name='AddNewsView'),
    path('edit_news/<int:pk>', views.EditNewsView.as_view(), name='EditNewsView'),
    path('newsitems/<int:pk>/add_comment', views.AddNewsComment.as_view(), name='AddNewsComment'),
    # path('login/', views.UserLoginView.as_view(), name='login'),
    # path('logout/', views.UserLogoutView.as_view(), name='logout'),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
