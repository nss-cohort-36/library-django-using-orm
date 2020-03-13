from django.conf.urls import url
from django.urls import path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^books$', book_list, name='books'),
    url(r'^book/form$', book_form, name='book_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    url(r'^books/(?P<book_id>[0-9]+)/form$', book_edit_form, name='book_edit_form'),

]
