# ar_delivery_uber_direct/conf.py
from django.conf import settings as django_settings


class Settings:
    @property
    def AR_DELIVERY_UBER_DIRECT_API_CLIENT_ID(self):
        return getattr(django_settings, "AR_DELIVERY_UBER_DIRECT_API_CLIENT_ID", None)

    @property
    def AR_DELIVERY_UBER_DIRECT_API_CLIENT_SECRET(self):
        return getattr(django_settings, "AR_DELIVERY_UBER_DIRECT_API_CLIENT_SECRET", None)

    @property
    def AR_DELIVERY_UBER_DIRECT_CUSTOMER_ID(self):
        return getattr(django_settings, "AR_DELIVERY_UBER_DIRECT_CUSTOMER_ID", None)

    @property
    def AR_DELIVERY_UBER_DIRECT_LOGIN_BASE_URL(self):
        return getattr(django_settings, "AR_DELIVERY_UBER_DIRECT_LOGIN_BASE_URL",
                       "https://login.uber.com/oauth/v2/token")

    @property
    def AR_DELIVERY_UBER_DIRECT_API_BASE_URL(self):
        return getattr(django_settings, "AR_DELIVERY_UBER_DIRECT_API_BASE_URL", "https://api.uber.com/v1")

    @property
    def AR_DELIVERY_UBER_DIRECT_ACCESS_TOKEN(self):
        return getattr(django_settings, "AR_DELIVERY_UBER_DIRECT_ACCESS_TOKEN", "AR_DELIVERY_UBER_DIRECT_ACCESS_TOKEN")


settings = Settings()
