# ARDelivery UberDirect

Librería de ARDelivery para usar con UberDirect en proyectos Django

## Descripción

Este paquete facilita la integración con la API de Uber Direct para gestionar entregas desde aplicaciones Django. Provee métodos para autenticación, cotización, creación, consulta, actualización y cancelación de entregas.

## Instalación

Puedes instalar el paquete directamente desde el repositorio Git:

```bash
pip install git+https://github.com/ArHoldings/ARDelivery_UberDirect.git@v0.1.0
```

## Requisitos

- Python >= 3.8
- Django (el paquete utiliza `django.conf.settings` y `django.core.cache`)
- requests

## Configuración

Agrega las siguientes variables en el archivo `settings.py` de tu proyecto Django:

```python
AR_DELIVERY_UBER_DIRECT_API_CLIENT_ID = "<tu_client_id>"
AR_DELIVERY_UBER_DIRECT_API_CLIENT_SECRET = "<tu_client_secret>"
AR_DELIVERY_UBER_DIRECT_CUSTOMER_ID = "<tu_customer_id>"
```

Opcionales (tienen valores por defecto):

```python
AR_DELIVERY_UBER_DIRECT_LOGIN_BASE_URL = "https://login.uber.com/oauth/v2/token"
AR_DELIVERY_UBER_DIRECT_API_BASE_URL = "https://api.uber.com/v1"
AR_DELIVERY_UBER_DIRECT_ACCESS_TOKEN = "AR_DELIVERY_UBER_DIRECT_ACCESS_TOKEN"
```

## Uso

Importa la clase principal:

```python
from ar_delivery_uber_direct import UberDirect
```

### Métodos disponibles

#### `UberDirect.create_quote(data)`

Solicita una cotización de entrega.

- **Parámetros:**  
  `data` (dict): Datos requeridos por la API de Uber Direct para cotizar.
- **Retorna:**  
  dict con la respuesta de la API.
- **Excepción:**  
  [`ar_delivery_uber_direct.exceptions.JsonException`](ar_delivery_uber_direct/exceptions.py) si ocurre un error.

#### `UberDirect.create_delivery(data)`

Crea una nueva entrega.

- **Parámetros:**  
  `data` (dict): Datos de la entrega.
- **Retorna:**  
  dict con la respuesta de la API.
- **Excepción:**  
  [`ar_delivery_uber_direct.exceptions.JsonException`](ar_delivery_uber_direct/exceptions.py) si ocurre un error.

#### `UberDirect.list_or_get_delivery(extra_data=None)`

Lista todas las entregas o consulta una entrega específica.

- **Parámetros:**  
  `extra_data` (dict o objeto): Si contiene `delivery_id`, consulta una entrega específica. Si es un dict, se usa como filtros para listar.
- **Retorna:**  
  dict con la respuesta de la API.
- **Excepción:**  
  [`ar_delivery_uber_direct.exceptions.JsonException`](ar_delivery_uber_direct/exceptions.py) si ocurre un error.

#### `UberDirect.update_delivery(delivery_id, data)`

Actualiza una entrega existente.

- **Parámetros:**  
  `delivery_id` (str): ID de la entrega.  
  `data` (dict): Datos a actualizar.
- **Retorna:**  
  dict con la respuesta de la API.
- **Excepción:**  
  [`ar_delivery_uber_direct.exceptions.JsonException`](ar_delivery_uber_direct/exceptions.py) si ocurre un error.

#### `UberDirect.cancel_delivery(delivery_id)`

Cancela una entrega.

- **Parámetros:**  
  `delivery_id` (str): ID de la entrega.
- **Retorna:**  
  dict con la respuesta de la API.
- **Excepción:**  
  [`ar_delivery_uber_direct.exceptions.JsonException`](ar_delivery_uber_direct/exceptions.py) si ocurre un error.

## Ejemplo de uso

```python
from ar_delivery_uber_direct import UberDirect

# Cotizar una entrega
quote = UberDirect.create_quote({
    "pickup": {...},
    "dropoff": {...},
    # otros campos requeridos
})

# Crear una entrega
delivery = UberDirect.create_delivery({
    "pickup": {...},
    "dropoff": {...},
    # otros campos requeridos
})

# Consultar una entrega específica
delivery_info = UberDirect.list_or_get_delivery({"delivery_id": "id_entrega"})

# Listar entregas
deliveries = UberDirect.list_or_get_delivery({"status": "active"})

# Actualizar una entrega
updated = UberDirect.update_delivery("id_entrega", {"field": "value"})

# Cancelar una entrega
cancelled = UberDirect.cancel_delivery("id_entrega")
```

## Manejo de errores

Todos los métodos lanzan [`ar_delivery_uber_direct.exceptions.JsonException`](ar_delivery_uber_direct/exceptions.py) en caso de error, con detalles en el atributo `json_data`.

---

Para más detalles revisa la implementación en [ar_delivery_uber_direct/uber_direct.py](ar_delivery_uber_direct/uber_direct.py).
