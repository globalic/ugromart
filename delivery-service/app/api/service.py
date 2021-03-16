import os
import httpx

ORDER_SERVICE_URL = "http://localhost:8002/api/v1/casts/"
DELIVERYSTATUS_SERVICE_URL = "http://localhost:8002/api/v1/casts/"
PAYMENT_SERVICE_URL = "http://localhost:8002/api/v1/casts/"


def is_payment_present(payment_id: int):
    url = os.environ.get("PAYMENT_SERVICE_URL") or PAYMENT_SERVICE_URL
    r = httpx.get(f"{url}{payment_id}")
    return True if r.status_code == 200 else False


def is_deliverystatus_present(deliverystatus_id: int):
    url = os.environ.get("DELIVERYSTATUS_SERVICE_URL") or DELIVERYSTATUS_SERVICE_URL
    r = httpx.get(f"{url}{deliverystatus_id}")
    return True if r.status_code == 200 else False


def is_order_present(order_id: int):
    url = os.environ.get("ORDER_SERVICE_URL") or ORDER_SERVICE_URL
    r = httpx.get(f"{url}{order_id}")
    return True if r.status_code == 200 else False
