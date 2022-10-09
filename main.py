from flask import Flask, request, jsonify
from time import time
import csv
import os

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello"


@app.route("/plot")
def plot():
    params = request.args
    data = params.get("data", None)
    if (data != None):
        s = data.split(",")
        if (not os.path.exists("data.csv")):
            with open("data.csv", "w") as data_csv:
                data_csv.write("time,temperature,humidity")
        with open("data.csv", "a") as data_csv:
            data_csv.write("\n" + str(time()) + "," + s[0] + "," + s[1])
            return "success"
    else:
        return "whops"

    return "whops"


@app.route("/data")
def data():
    d = {}
    if (not os.path.exists("data.csv")):
        return jsonify(d)
    with open("data.csv", "r") as data_csv:
        reader = csv.reader(data_csv)
        for row in reader:
            d[row[0]] = {"temperature": row[1], "humidity": row[2]}
        return jsonify(d)


if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=8080, debug=True)
