from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
DATA_PATH = "data/almaty_climate.csv"
IMG_PATH = "static"

def create_graphs():
    df = pd.read_csv(DATA_PATH)

    plt.figure()
    plt.plot(df["Month"], df["Temperature (°C)"], marker='o')
    plt.title("Температура в Алматы")
    plt.xlabel("Месяц")
    plt.ylabel("Температура (°C)")
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_PATH, "temperature.png"))
    plt.close()

    plt.figure()
    plt.bar(df["Month"], df["Precipitation (mm)"], color='skyblue')
    plt.title("Осадки в Алматы")
    plt.xlabel("Месяц")
    plt.ylabel("Осадки (мм)")
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_PATH, "precipitation.png"))
    plt.close()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/temperature")
def temperature():
    create_graphs()
    return render_template("temperature.html")

@app.route("/precipitation")
def precipitation():
    create_graphs()
    return render_template("precipitation.html")

@app.route("/table")
def table():
    return render_template("table.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
