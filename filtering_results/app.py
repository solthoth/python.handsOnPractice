import csv
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/laureates/")
def laureate():
    results = []
    if not request.args.get("flName"):
        return jsonify(results)

    search_string = request.args.get("flName").lower().strip()
    for laureate in laureates:
        surname = laureate["surname"].lower()
        name = laureate["name"].lower()
        if (search_string in surname) or (search_string in name):
            results.append(laureate)

    return jsonify(results)

app.run(debug=True)