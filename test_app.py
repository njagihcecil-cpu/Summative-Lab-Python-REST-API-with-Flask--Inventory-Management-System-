from app import app

client = app.test_client()


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_get_inventory():
    response = client.get("/inventory")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_get_single_item():
    response = client.get("/inventory/1")
    assert response.status_code == 200
    assert response.get_json()["id"] == 1


def test_get_invalid_item():
    response = client.get("/inventory/999")
    assert response.status_code == 404


def test_add_item():
    new_item = {
        "barcode": "123456789",
        "name": "Test Product",
        "brand": "Test Brand",
        "price": 100,
        "stock": 10
    }

    response = client.post("/inventory", json=new_item)

    assert response.status_code == 201
    assert response.get_json()["name"] == "Test Product"


def test_update_item():
    updates = {
        "price": 999,
        "stock": 99
    }

    response = client.patch("/inventory/1", json=updates)

    assert response.status_code == 200

    data = response.get_json()
    assert data["price"] == 999
    assert data["stock"] == 99


def test_delete_item():
    response = client.delete("/inventory/2")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Item deleted successfully"


def test_delete_invalid_item():
    response = client.delete("/inventory/999")

    assert response.status_code == 404

def test_lookup_product():
    response = client.get("/lookup/3017620422003")

    assert response.status_code in [200, 404]