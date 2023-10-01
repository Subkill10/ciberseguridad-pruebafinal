from flask import Flask
from currentweather_data_fetcher import get_wind_spped

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



@app.route("/api/")
def hello_api():
    return get_wind_spped("Quito,Ec")

@app.route("/api/")
def hello_api():
    return get_wind_spped("Quito,Ec")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)