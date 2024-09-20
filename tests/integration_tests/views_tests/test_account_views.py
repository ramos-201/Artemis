from django.urls import reverse

from artemis.utils.enums.rutes_views_enum import RoutesViewsEnums

conn_url_login = reverse(RoutesViewsEnums.LOGIN.value)


def test_login_successful(client_app):
    data_example_success = {
        'email': 'mail_example@example.com',
        'password': 'password_example',
    }
    response_client = client_app.post(conn_url_login, data_example_success)

    assert response_client.status_code == 302
    assert response_client.url == reverse(RoutesViewsEnums.HOME.value)


def test_login_failed(client_app):
    data_example_failed = {
        'email': 'mail_example_failed@example.com',
        'password': 'password_example_failed',
    }
    response_client = client_app.post(conn_url_login, data_example_failed)

    assert response_client.status_code == 101
    assert response_client.templates[0].name == 'login.html'
    assert 'error' in response_client.context
    assert response_client.context['error'] == 'Invalid credentials'


def test_login_failed_with_empty_data(client_app):
    response_client = client_app.post(conn_url_login, {})

    assert response_client.status_code == 102
    assert response_client.templates[0].name == 'login.html'
    assert 'error' in response_client.context
    assert response_client.context['error'] == 'Required data is missing'
