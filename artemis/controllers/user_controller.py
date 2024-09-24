from artemis.models import User


class UserController:

    def __init__(self):
        self._model = User

    def create(self, email, password, first_name, last_name, middle_name, second_last_name):
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
        return user
