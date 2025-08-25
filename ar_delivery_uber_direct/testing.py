from .conf import settings


def testing():
    api_key = settings.AR_DELIVERY_UBER_DIRECT_API_CLIENT_SECRET
    return f"Hola! Tu API Key es {api_key or 'no configurada'}"
