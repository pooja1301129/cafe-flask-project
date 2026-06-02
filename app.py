from flask import Flask, render_template, request

app = Flask(__name__)

menu = {
    "pizza": 50,
    "burger": 100,
    "salad": 30,
    "popcorn": 40
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bill", methods=["POST"])
def bill():
    items = request.form.get("items")
    total = 0
    bill_items = []

    if items:
        item_list = items.lower().split(",")

        for item in item_list:
            item = item.strip()

            if item in menu:
                total += menu[item]
                bill_items.append(item)
            else:
                bill_items.append(item + " (not available)")

    return render_template("index.html",
                           total=total,
                           bill_items=bill_items)

if __name__ == "__main__":
    app.run(debug=True)