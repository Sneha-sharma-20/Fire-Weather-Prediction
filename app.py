from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
ridge_model = joblib.load("ridge.pkl")
scaler = joblib.load("scaler.pkl")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    features = [
        float(request.form["Temperature"]),
        float(request.form["RH"]),
        float(request.form["Ws"]),
        float(request.form["Rain"]),
        float(request.form["FFMC"]),
        float(request.form["DMC"]),
        float(request.form["DC"]),
        float(request.form["ISI"]),
        float(request.form["BUI"]),
    ]

    input_data = np.array(features).reshape(1, -1)
    input_scaled = scaler.transform(input_data)
    prediction = ridge_model.predict(input_scaled)[0]

    if prediction <= 5:
        risk = "Low Fire Risk"
        risk_class = "low"
        causes = [
            "High moisture content in vegetation",
            "Low temperature and wind conditions",
            "Recent rainfall reducing fuel dryness",
        ]
        precautions = [
            "Normal outdoor activities are safe",
            "Continue routine forest monitoring",
            "Maintain basic fire safety awareness",
        ]

    elif prediction <= 12:
        risk = "Moderate Fire Risk"
        risk_class = "moderate"
        causes = [
            "Moderate drying of surface fuels",
            "Slight increase in temperature or wind",
            "Limited recent rainfall",
        ]
        precautions = [
            "Avoid unattended campfires",
            "Follow basic fire safety guidelines",
            "Monitor weather conditions closely",
        ]

    elif prediction <= 25:
        risk = "High Fire Risk"
        risk_class = "high"
        causes = [
            "Dry surface and subsurface fuels",
            "High temperature and low humidity",
            "Strong wind conditions",
        ]
        precautions = [
            "Restrict open fires and burning activities",
            "Keep firefighting resources ready",
            "Issue public fire warnings",
        ]

    elif prediction <= 50:
        risk = "Very High Fire Risk"
        risk_class = "very-high"
        causes = [
            "Extremely dry vegetation",
            "Persistent high temperatures",
            "Very strong winds accelerating fire spread",
        ]
        precautions = [
            "Impose fire bans",
            "Limit access to forest areas",
            "Deploy emergency response teams",
        ]

    else:
        risk = "Extreme Fire Risk"
        risk_class = "extreme"
        causes = [
            "Severe drought conditions",
            "Highly combustible forest fuels",
            "Extreme heat and wind intensity",
        ]
        precautions = [
            "Declare emergency conditions",
            "Evacuate high-risk zones",
            "Activate disaster management protocols",
        ]
    return render_template(
        "home.html",
        prediction=round(prediction, 2),
        risk=risk,
        risk_class=risk_class,
        causes=causes,
        precautions=precautions,
    )


if __name__ == "__main__":
    app.run(debug=True)
