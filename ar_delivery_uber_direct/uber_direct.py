# ar_delivery_uber_direct/uber_direct.py

import json
from datetime import datetime, timedelta
from functools import wraps

import requests
from django.core.cache import cache

from .conf import settings
from .exceptions import JsonException


def _token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cached = cache.get(settings.AR_DELIVERY_UBER_DIRECT_ACCESS_TOKEN, None)

        if cached is None or UberDirect._cached_token_expires_soon(json.loads(cached)):
            token_json = UberDirect._get_new_token()
            new_token = token_json['access_token']
            expires_in = token_json.get('expires_in', 1800)
            expires_at = datetime.now() + timedelta(seconds=expires_in)

            token_data = {
                'access_token': new_token,
                'expires_at': expires_at
            }

            cache_timeout = expires_in - 60 if expires_in > 60 else expires_in
            cache.set(
                settings.AR_DELIVERY_UBER_DIRECT_ACCESS_TOKEN,
                json.dumps(token_data, default=UberDirect._convert_datetime),
                timeout=cache_timeout
            )
            cached = cache.get(settings.AR_DELIVERY_UBER_DIRECT_ACCESS_TOKEN)

        token = json.loads(cached)['access_token']

        headers = kwargs.get("headers", {}) or {}
        headers["Authorization"] = f"Bearer {token}"
        kwargs["headers"] = headers

        return func(*args, **kwargs)

    return wrapper


class UberDirect:
    """
    Cliente para integrar AR Delivery Uber Direct en proyectos Django.
    Maneja autenticación, cache de tokens y solicitudes.
    """

    @staticmethod
    def _cached_token_expires_soon(cached_token):
        expires_at = datetime.strptime(cached_token['expires_at'], '%Y-%m-%dT%H:%M:%S.%f')
        return (expires_at - datetime.now()) < timedelta(minutes=1)

    @staticmethod
    def _convert_datetime(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError("Tipo de objeto no serializable")

    @staticmethod
    def _get_new_token():
        url = f'{settings.AR_DELIVERY_UBER_DIRECT_LOGIN_BASE_URL}'
        payload = {
            'client_id': settings.AR_DELIVERY_UBER_DIRECT_API_CLIENT_ID,
            'client_secret': settings.AR_DELIVERY_UBER_DIRECT_API_CLIENT_SECRET,
            'grant_type': 'client_credentials',
            'scope': 'eats.deliveries'
        }
        response = requests.post(url, data=payload)

        try:
            data = response.json()
        except Exception:
            data = {"error": response.text}

        if response.status_code == 200:
            return data

        # Lanzar excepción con JSON
        raise JsonException(
            json_data={
                "error": "Token Error",
                "status_code": response.status_code,
                "details": data
            },
            status_code=response.status_code
        )

    @staticmethod
    @_token_required
    def create_quote(data, headers=None):
        url = f'{settings.AR_DELIVERY_UBER_DIRECT_API_BASE_URL}/customers/{settings.AR_DELIVERY_UBER_DIRECT_CUSTOMER_ID}/delivery_quotes'
        headers = headers or {}
        if not 'Content-Type' in headers:
            headers['Content-Type'] = 'application/json; charset=utf-8'

        response = requests.post(url, data=data, headers=headers)

        try:
            data = response.json()
        except Exception:
            data = {"error": response.text}

        if response.status_code == 200:
            return data

        # Lanzar excepción con JSON
        raise JsonException(
            json_data={
                "error": "Create Quote Error",
                "status_code": response.status_code,
                "details": data
            },
            status_code=response.status_code
        )

    @staticmethod
    @_token_required
    def create_delivery(data, headers=None):
        url = f'{settings.AR_DELIVERY_UBER_DIRECT_API_BASE_URL}/customers/{settings.AR_DELIVERY_UBER_DIRECT_CUSTOMER_ID}/deliveries'
        headers = headers or {}
        if not 'Content-Type' in headers:
            headers['Content-Type'] = 'application/json; charset=utf-8'

        response = requests.post(url, data=data, headers=headers)

        try:
            data = response.json()
        except Exception:
            data = {"error": response.text}

        if response.status_code == 200:
            return data

        # Lanzar excepción con JSON
        raise JsonException(
            json_data={
                "error": "Create Delivery Error",
                "status_code": response.status_code,
                "details": data
            },
            status_code=response.status_code
        )

    @staticmethod
    @_token_required
    def list_or_get_delivery(extra_data=None, headers=None):
        base_url = f"{settings.AR_DELIVERY_UBER_DIRECT_API_BASE_URL}/customers/{settings.AR_DELIVERY_UBER_DIRECT_CUSTOMER_ID}/deliveries"

        delivery_id = getattr(extra_data, "delivery_id", None)
        query = None

        # Construir URL según delivery_id
        if delivery_id:
            url = f"{base_url}/{delivery_id}"
        else:
            url = base_url
            query = extra_data  # se usa como diccionario de filtros

        headers = headers or {}
        if not 'Content-Type' in headers:
            headers['Content-Type'] = 'application/json; charset=utf-8'

        # Hacer request
        response = requests.get(url, headers=headers, params=query)

        try:
            data = response.json()
        except Exception:
            data = {"error": response.text}

        if response.status_code == 200:
            return data

        raise JsonException(
            json_data={
                "error": "List or Get Delivery Error",
                "status_code": response.status_code,
                "details": data,
            },
            status_code=response.status_code,
        )

    @staticmethod
    @_token_required
    def update_delivery(delivery_id, data, headers=None):
        url = f"{settings.AR_DELIVERY_UBER_DIRECT_API_BASE_URL}/customers/{settings.AR_DELIVERY_UBER_DIRECT_CUSTOMER_ID}/deliveries/{delivery_id}"

        headers = headers or {}
        if not 'Content-Type' in headers:
            headers['Content-Type'] = 'application/json; charset=utf-8'

        response = requests.post(url, data=data, headers=headers)

        try:
            data = response.json()
        except Exception:
            data = {"error": response.text}

        if response.status_code == 200:
            return data

        raise JsonException(
            json_data={
                "error": "Update Delivery Error",
                "status_code": response.status_code,
                "details": data,
            },
            status_code=response.status_code,
        )

    @staticmethod
    @_token_required
    def cancel_delivery(delivery_id, headers=None):
        url = f"{settings.AR_DELIVERY_UBER_DIRECT_API_BASE_URL}/customers/{settings.AR_DELIVERY_UBER_DIRECT_CUSTOMER_ID}/deliveries/{delivery_id}/cancel"

        headers = headers or {}
        if not 'Content-Type' in headers:
            headers['Content-Type'] = 'application/json; charset=utf-8'

        response = requests.post(url, headers=headers)

        try:
            data = response.json()
        except Exception:
            data = {"error": response.text}

        if response.status_code == 200:
            return data

        raise JsonException(
            json_data={
                "error": "Cancel Delivery Error",
                "status_code": response.status_code,
                "details": data,
            },
            status_code=response.status_code,
        )
