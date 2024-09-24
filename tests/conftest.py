from pytest import fixture
from django.test import Client

from artemis.models import User
from tests.factory import UserFactory


@fixture(autouse=True)
def db_clean(db):
    User.objects.all().delete()


@fixture
def client_app():
    return Client()


@fixture
def user_created():
    user = UserFactory.create()
    user.set_password('password_example')
    user.save()
    return user
