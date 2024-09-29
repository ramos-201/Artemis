from django.urls import path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from artemis.utils.enums.rutes_views_enum import RoutesViewsEnums
from artemis.api.account_view import register_user_view, login_view


@api_view(['GET'])
@permission_classes([AllowAny])
def conn_view(request):
    return Response({'message': 'Connection established'}, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_conn_view(request):
    return Response({'message': 'Connection protected established'}, status=200)


urlpatterns = [
    path('conn/', conn_view, name='conn'),
    path('protected-conn/', protected_conn_view, name='conn-p'),

    path('login/', login_view, name=RoutesViewsEnums.LOGIN.value),
    path('register/', register_user_view, name=RoutesViewsEnums.REGISTER.value),
]
