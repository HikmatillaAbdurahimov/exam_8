from django.contrib.auth.models import UserManager


class CustomerManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_customer=True)
