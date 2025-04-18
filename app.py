
from flask import Flask, request, jsonify

app = Flask(__name__)

# Manually assigned coefficients from Part 1 regression
INTERCEPT = 141.58
COEF_TREATMENT = -9.11
COEF_SPENDING = -0.46

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        treatment = data["treatment"]
        spending = data["sustainability_spending"]

        # Predict using linear model
        y_hat = INTERCEPT + COEF_TREATMENT * treatment + COEF_SPENDING * spending

        return jsonify({
            "predicted_engagement_score": round(y_hat, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
