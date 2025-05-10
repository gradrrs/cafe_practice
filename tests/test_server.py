from server.app.services import calculate_total

def test_calculate_total():
    assert calculate_total(5.5, 2) == 11.0