from client.model.order_model import Order

def test_order_model():
    order = Order("Coffee", 2)
    assert order.item_name == "Coffee"
    assert order.quantity == 2