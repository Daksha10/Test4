from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual API key
API_KEY = "4b63527d54819c566f06c679a758131c"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        phone_number = request.form.get("phone_number")
        if not phone_number:
            return render_template("index.html", error="Please enter a phone number.")

        url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={phone_number}"
        response = requests.get(url)
        data = response.json()

        if "success" in data and not data["success"]:
            return render_template("index.html", error="Invalid API key or request limit exceeded.")

        return render_template("index.html", result=data)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
