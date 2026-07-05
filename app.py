from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Welcome to my Inventory Management API!"
    }

if __name__ == "__main__":
    app.run(debug=True)