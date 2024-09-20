from pytest import fixture
from django.test import Client

from tests.factory import UserFactory


@fixture
def client_app():
    return Client()


@fixture
def user_created():
    user = UserFactory.create()
    user.set_password('password_example')
    user.save()
    yield user
    user.delete()
