from django.test import Client
from django.urls import reverse


def test_stable_connection():
    client = Client()
    conn_url = reverse('conn')
    response_conn = client.get(conn_url)

    assert response_conn.status_code == 200
    assert response_conn.content == b'Connection established'
