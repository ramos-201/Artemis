from django.http import HttpResponse
from django.urls import path

from artemis.utils.enums.rutes_views_enum import RoutesViewsEnums
from artemis.api.account_view import register_user_view, login_view


def conn_view(request):
    return HttpResponse('Connection established')


urlpatterns = [
    path('conn/', conn_view, name='conn'),
    path('home/', conn_view, name=RoutesViewsEnums.HOME.value),

    path('api/login/', login_view, name=RoutesViewsEnums.LOGIN.value),
    path('api/register/', register_user_view, name=RoutesViewsEnums.REGISTER.value)
]
