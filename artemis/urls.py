from django.http import HttpResponse
from django.urls import path


def conn_view(request):
    return HttpResponse('Connection established')


urlpatterns = [
    path('conn/', conn_view, name='conn'),
]
