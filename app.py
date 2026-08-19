from flask import Flask, render_template, request

app = Flask(__name__)
def recommend_crop(n, p, k, temperature, humidity, ph, rainfall):

    if rainfall > 200 and humidity > 70 and temperature < 30:
        return "Rice 🌾"

    elif temperature > 25 and rainfall > 100 and humidity > 50:
        return "Cotton 🌿"

    elif temperature > 20 and rainfall > 80 and ph >= 6:
        return "Maize 🌽"

    elif temperature < 25 and rainfall < 100 and ph >= 6:
        return "Wheat 🌾"

    elif humidity > 60 and rainfall > 100:
        return "Sugarcane 🎋"

    elif temperature > 25 and rainfall < 80:
        return "Millet 🌾"

    else:
        return "Maize 🌽"

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
@app.route("/crop_recommendation", methods=["GET", "POST"])
@app.route("/crop-recommendation", methods=["GET", "POST"])
def crop_recommendation():

    if request.method == "POST":

        nitrogen = float(request.form["nitrogen"])
        phosphorus = float(request.form["phosphorus"])
        potassium = float(request.form["potassium"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        recommendation = recommend_crop(
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        )

        return render_template(
            "crop_recommendation.html",
            recommendation=recommendation
        )


        return render_template(
            "crop_recommendation.html",
            recommendation="Rice"
        )

    return render_template("crop_recommendation.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
