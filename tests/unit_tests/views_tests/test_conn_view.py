from pytest import mark
from django.urls import reverse

from artemis.models import User


def test_stable_connection(client_app):
    conn_url = reverse('conn')
    response_conn = client_app.get(conn_url)

    assert response_conn.status_code == 200
    assert response_conn.content == b'{"message":"Connection established"}'


@mark.django_db
def test_protected_connection(client_app):
    User.objects.create_user(email='mail_example@example.com', password='password_example')
    client_app.login(username='mail_example@example.com', password='password_example')

    conn_protected_url = reverse('conn-p')
    response = client_app.get(conn_protected_url)

    assert response.status_code == 200
    assert response.json().get('message') == 'Connection protected established'
