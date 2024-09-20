from django.shortcuts import redirect, render

from artemis.utils.enums.rutes_views_enum import RoutesViewsEnums


def login_conn_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            return render(request, 'login.html', {'error': 'Required data is missing'}, status=102)

        if email == 'mail_example@example.com' and password == 'password_example':
            return redirect(RoutesViewsEnums.HOME.value)
        return render(request, 'login.html', {'error': 'Invalid credentials'}, status=101)

    return redirect(RoutesViewsEnums.LOGIN.value)  # load page
