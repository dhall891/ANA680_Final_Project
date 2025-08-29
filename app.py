from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = np.array(features).reshape(1, -1)
    final_scaled = scaler.transform(final_features)
    prediction = model.predict(final_scaled)[0]
    output = "Heart Disease" if prediction == 1 else "No Heart Disease"
    return render_template('index.html', prediction_text=f'Result: {output}')

if __name__ == "__main__":
    app.run(debug=True)
