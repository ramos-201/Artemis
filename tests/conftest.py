from pytest import fixture
from django.test import Client


@fixture
def client_app():
    return Client()
