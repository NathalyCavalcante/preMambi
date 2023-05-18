from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
    path('new/<int:worker_pk>/',views.new_conversation, name='new'),
]

# importa para o main url file que é a do premambi