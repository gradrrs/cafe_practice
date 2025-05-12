import requests

SERVER_URL = "http://127.0.0.1:5000"

def fetch_menu():
    return requests.get(f"{SERVER_URL}/menu").json()

def send_order(item_name, quantity):
    return requests.post(f"{SERVER_URL}/order", json={
        "item_name": item_name,
        "quantity": quantity
    }).json()