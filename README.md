# ARDelivery UberDirect

Librería de ARDelivery para usar con UberDirect en proyectos Django


## Descripción

Este paquete facilita la integración con la API de Uber Direct para gestionar entregas desde aplicaciones Django.


## Instalación

Puedes instalar el paquete directamente desde el repositorio Git:

```bash
pip install git+https://github.com/ArHoldings/ARDelivery_UberDirect.git
```

## Configuración

Para usar esta librería, se debe configurar las variables necesarias en el archivo `settings.py` de tu proyecto Django. Estas variables permiten que el paquete acceda a las credenciales y URLs necesarias para funcionar correctamente.

Ejemplo:

```python
AR_DELIVERY_UBER_DIRECT_API_CLIENT_ID = "<tu_client_id>"
AR_DELIVERY_UBER_DIRECT_API_CLIENT_SECRET = "<tu_client_secret>"
AR_DELIVERY_UBER_DIRECT_CUSTOMER_ID = "<tu_customer_id>"
```
## Opcional
Variables opcionales (tienen valores por defecto, pero puedes personalizarlas):

```python
AR_DELIVERY_UBER_DIRECT_LOGIN_BASE_URL = "https://login.uber.com/oauth/v2/token"
AR_DELIVERY_UBER_DIRECT_API_BASE_URL = "https://api.uber.com/v1"
AR_DELIVERY_UBER_DIRECT_ACCESS_TOKEN = "AR_DELIVERY_UBER_DIRECT_ACCESS_TOKEN"
```