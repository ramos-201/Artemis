from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from artemis.controllers.user_controller import UserController


@api_view(['POST'])
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


def register_conn_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        second_last_name = request.POST.get('second_last_name')

        _, error = UserController().create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            second_last_name=second_last_name
        )

        if error:
            return render(request, 'register.html', {'error': error})

        return redirect('login')

    return render(request, 'register.html')
