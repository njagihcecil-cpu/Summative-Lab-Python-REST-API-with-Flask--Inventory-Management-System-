import requests

BASE_URL = "http://127.0.0.1:5000"

def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")

    if response.status_code == 200:
        items = response.json()

        for item in items:
            print(item)
    else:
        print("Error retrieving inventory.")

def add_item():

    barcode = input("Barcode: ")
    name = input("Name: ")
    brand = input("Brand: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    item = {
        "barcode": barcode,
        "name": name,
        "brand": brand,
        "price": price,
        "stock": stock
    }

    response = requests.post(f"{BASE_URL}/inventory", json=item)

    print(response.json())

def update_item():

    item_id = input("Item ID: ")

    price = float(input("New Price: "))
    stock = int(input("New Stock: "))

    updates = {
        "price": price,
        "stock": stock
    }

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=updates
    )

    print(response.json())

def delete_item():

    item_id = input("Item ID: ")

    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    print(response.json())

def lookup_product():

    barcode = input("Barcode: ")

    response = requests.get(
        f"{BASE_URL}/lookup/{barcode}"
    )

    print(response.json())

while True:

    print("\n===== Inventory System =====")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Lookup Product")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        view_inventory()

    elif choice == "2":
        add_item()

    elif choice == "3":
        update_item()

    elif choice == "4":
        delete_item()

    elif choice == "5":
        lookup_product()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")