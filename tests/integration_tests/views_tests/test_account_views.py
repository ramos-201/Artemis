from pytest import mark
from django.urls import reverse

from artemis.models import User
from artemis.utils.enums.rutes_views_enum import RoutesViewsEnums

conn_url_login = reverse(RoutesViewsEnums.LOGIN.value)


@mark.django_db
def test_login_successful(client_app, user_created):
    data_example_success = {
        'email': 'mail_example@example.com',
        'password': 'password_example',
    }
    response_client = client_app.post(conn_url_login, data_example_success)

    assert response_client.status_code == 302
    assert response_client.url == reverse(RoutesViewsEnums.HOME.value)
    assert client_app.session['_auth_user_id'] == str(user_created.id)


@mark.django_db
def test_login_failed(client_app):
    data_example_failed = {
        'email': 'mail_example_failed@example.com',
        'password': 'password_example_failed',
    }
    response_client = client_app.post(conn_url_login, data_example_failed)

    assert response_client.status_code == 200
    assert response_client.templates[0].name == 'login.html'
    assert 'error' in response_client.context
    assert response_client.context['error'] == 'Invalid credentials'


def test_login_failed_with_empty_data(client_app):
    response_client = client_app.post(conn_url_login, {})

    assert response_client.status_code == 200
    assert response_client.templates[0].name == 'login.html'
    assert 'error' in response_client.context
    assert response_client.context['error'] == 'Required data is missing'


conn_url_register = reverse('register')

data_example = {
    'email': 'mail_example@example.com',
    'password': 'password_example',
    'first_name': 'Juan',
    'last_name': 'Gomez',
    'middle_name': 'Camilo',
    'second_last_name': 'Silva',
}


@mark.django_db
def test_register_new_user_successfully(client_app):
    response_client = client_app.post(conn_url_register, data_example)
    assert response_client.status_code == 302
    assert response_client.url == reverse(RoutesViewsEnums.LOGIN.value)

    result_user = User.objects.filter(email=data_example['email']).first()
    assert result_user.email == data_example['email']
    assert result_user.password is not None
    assert result_user.first_name == data_example['first_name']
    assert result_user.last_name == data_example['last_name']
    assert result_user.middle_name == data_example['middle_name']
    assert result_user.second_last_name == data_example['second_last_name']
    assert result_user.is_active is True
    assert result_user.created_at is not None
    assert result_user.modified_at is not None


def test_error_registering_existing_user(client_app, user_created):
    response_client = client_app.post(conn_url_register, data_example)
    assert response_client.status_code == 200
    assert response_client.templates[0].name == 'register.html'
    assert 'error' in response_client.context
    assert response_client.context['error'] == 'This email is already registered'


def test_error_registering_user_with_empty_data(client_app):
    response_client = client_app.post(conn_url_register, {})
    assert response_client.status_code == 200
    assert response_client.templates[0].name == 'register.html'
    assert 'error' in response_client.context
    assert response_client.context['error'] == 'Required data is missing'


@mark.django_db
def test_register_user_successfully_without_any_unnecessary_data(client_app):
    data_example_modified = data_example.copy()
    data_example_modified.pop('middle_name')
    data_example_modified.pop('second_last_name')
    response_client = client_app.post(conn_url_register, data_example_modified)

    assert response_client.status_code == 302
    assert response_client.url == reverse(RoutesViewsEnums.LOGIN.value)

    result_user = User.objects.filter(email=data_example['email']).first()
    assert result_user.email == data_example['email']


def test_error_with_email_format_when_registering_user(client_app):
    data_example_modified = data_example.copy()
    data_example_modified['email'] = 'test_example_failed'
    response_client = client_app.post(conn_url_register, data_example_modified)

    assert response_client.status_code == 200
    assert response_client.templates[0].name == 'register.html'
    assert 'error' in response_client.context
    assert response_client.context['error'] == 'Email format is not valid'
