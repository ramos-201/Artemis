import re

from django.db import IntegrityError

from artemis.models import User


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))


class UserController:

    def __init__(self):
        self._model = User

    def create_user(self, email, password, first_name, last_name, middle_name, second_last_name):
        if not email or not password or not first_name or not last_name:
            return None, 'Required data is missing'

        if not is_valid_email(email):
            return None, 'Email format is not valid'

        try:
            user = self._model.objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                second_last_name=second_last_name,
                is_active=True,
                is_superuser=False
            )

            user.set_password(password)
            user.save()
            return user, None

        except IntegrityError as exc:
            if 'duplicate key value violates unique constraint' in str(exc):
                return None, 'This email is already registered'
