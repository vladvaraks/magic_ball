from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class LoginBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.save()
        return user
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None