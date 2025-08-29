from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect form inputs
    features = [float(x) for x in request.form.values()]
    final_features = np.array(features).reshape(1, -1)

    # Scale and predict
    final_scaled = scaler.transform(final_features)
    prediction = model.predict(final_scaled)[0]

    # Map result
    output = "Heart Disease" if prediction == 1 else "No Heart Disease"

    return render_template('index.html', prediction=output)

if __name__ == "__main__":
    app.run(debug=True)
