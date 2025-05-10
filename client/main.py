from client.controller.order_controller import OrderController
from client.view.main_view import MainView

if __name__ == "__main__":
    controller = OrderController()
    app = MainView(controller)
    app.run()