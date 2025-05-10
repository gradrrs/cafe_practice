from client.utils.api_client import fetch_menu, send_order

class OrderController:
    def __init__(self):
        self.menu = []

    def load_menu(self):
        self.menu = fetch_menu()
        return self.menu

    def submit_order(self, item_name, quantity):
        return send_order(item_name, quantity)