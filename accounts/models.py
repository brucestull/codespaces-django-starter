from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Model for user. This class extends `AbstractUser` and makes possible
    the addition of custom fields.
    """

    def __str__(self):
        """
        Returns string representation of `CustomUser` object.

        `str()` has been wrapped around `self.username` to eliminate
        `__str__ does not return strpylint(invalid-str-returned)`
        linting error. This `str()` will be removed in the future.
        """
        return str(self.username)
