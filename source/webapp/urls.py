from django.urls import path

from webapp.views import (index_view,
                          add_note
                          )

urlpatterns = [
    path('', index_view, name="index"),
    path('note/add/', add_note, name='add_note')
]
