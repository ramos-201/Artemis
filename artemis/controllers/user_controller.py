from django.db import IntegrityError

from artemis.models import User


class UserController:

    def __init__(self):
        self._model = User

    def create_user(self, email, password, first_name, last_name, middle_name=None, second_last_name=None):
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
