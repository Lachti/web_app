from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', login_required(views.index), name='index'),
    url(r'^return_book/(?P<book_id>\d)/$', login_required(views.return_book), name='return_book'),
    url(r'^rent_book/(?P<book_id>\d)/$', login_required(views.rent_book), name='rent_book'),
]

