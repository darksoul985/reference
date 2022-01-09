from django.urls import path
from spravka import views as spravka


app_name = 'spravka'

urlpatterns = [
    path('', spravka.printing_message)
]
