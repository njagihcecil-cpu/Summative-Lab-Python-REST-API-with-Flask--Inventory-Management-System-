from flask import Flask, request, jsonify
from inventory import inventory

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Welcome to my Inventory Management API!"
    }

@app.route("/inventory")
def get_inventory():
    return inventory

@app.route("/inventory/<int:item_id>")
def get_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return item

    return {"error": "Item not found"}, 404

@app.route("/inventory", methods=["POST"])
def add_item():
    new_item = request.json

    inventory.append(new_item)

    return new_item, 201

@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):

    updates = request.json

    for item in inventory:

        if item["id"] == item_id:

            item.update(updates)

            return item

    return {"error": "Item not found"}, 404

@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):

    for item in inventory:

        if item["id"] == item_id:

            inventory.remove(item)

            return {"message": "Item deleted"}

    return {"error": "Item not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)