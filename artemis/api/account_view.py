import re

from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from artemis.controllers.user_controller import UserController


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Required data is missing'}, status=400)

    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=200)

    return Response({'error': 'Invalid credentials'}, status=400)


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
