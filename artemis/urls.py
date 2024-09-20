from django.http import HttpResponse
from django.urls import path

from artemis.utils.enums.rutes_views_enum import RoutesViewsEnums
from artemis.views.account_view import login_conn_view


def conn_view(request):
    return HttpResponse('Connection established')


urlpatterns = [
    path('conn/', conn_view, name='conn'),

    path('home/', conn_view, name=RoutesViewsEnums.HOME.value),
    path('login/', login_conn_view, name=RoutesViewsEnums.LOGIN.value),

]
