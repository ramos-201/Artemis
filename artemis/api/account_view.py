import re

from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from artemis.api.serializers.model_serializers import UserSerializer
from artemis.api.serializers.response_api import RequiredDataException, InvalidCredentialsException, SuccessResponse
from artemis.controllers.user_controller import UserController


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):

    required_fields = ['email', 'password']
    missing_fields = [field for field in required_fields if not request.data.get(field)]

    if missing_fields:
        return RequiredDataException(missing_fields)

    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        user_serializer = UserSerializer(user)
        return SuccessResponse('Login successful', user_serializer.data)

    return InvalidCredentialsException(required_fields)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user_view(request):
    required_fields = ['email', 'password', 'first_name', 'last_name']
    missing_fields = [field for field in required_fields if field not in request.data]

    if missing_fields:
        return Response({'error': 'Required data is missing'}, status=400)

    email = request.data.get('email')
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if not re.match(email_regex, email):
        return Response({'error': 'Email format is not valid'}, status=400)

    _, error = UserController().create_user(
        email=request.POST.get('email'),
        password=request.POST.get('password'),
        first_name=request.POST.get('first_name'),
        last_name=request.POST.get('last_name'),
        middle_name=request.POST.get('middle_name'),
        second_last_name=request.POST.get('second_last_name')
    )

    if error:
        return Response({'error': error}, status=400)

    return Response({'message': 'User created successfully'}, status=200)
