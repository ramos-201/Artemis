from factory.django import DjangoModelFactory

from artemis.models import User


class UserFactory(DjangoModelFactory):
    email = 'mail_example@example.com'
    password = 'password_example'
    first_name = 'first_name_example'
    last_name = 'last_name_example'
    middle_name = 'middle_name_example'
    second_last_name = 'second_last_name_example'
    # created_at = ...
    # modified_at = ...
    is_active = True
    is_superuser = False

    class Meta:
        model = User
