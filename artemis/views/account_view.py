from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from artemis.controllers.user_controller import UserController
from artemis.utils.enums.rutes_views_enum import RoutesViewsEnums


def login_conn_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            return render(request, 'login.html', {'error': 'Required data is missing'}, status=102)

        user_auth = authenticate(request, email=email, password=password)

        if user_auth is not None:
            login(request, user_auth)
            return redirect('home')

        return render(request, 'login.html', {'error': 'Invalid credentials'}, status=101)

    return redirect(RoutesViewsEnums.LOGIN.value)  # load page


def register_conn_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        second_last_name = request.POST.get('second_last_name')

        _ = UserController().create(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            second_last_name=second_last_name
        )
        return redirect('login')

    return render(request, 'register.html')
