from django.urls import path

from . import views


app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('by_author/', views.select_by_author, name='select_by_author'),
    path('author/<int:author_id>', views.quotes_by_author, name='quotes_by_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('add_author/', views.add_author, name='add_author'),
    path('about_author/<int:quote_id>', views.about_author, name='about_author'),
    path('tag/<int:tag_id>', views.select_by_tag, name='select_by_tag'),
]