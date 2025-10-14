from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

model = joblib.load('models\trained_model.pkl')

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/predict', methods=['POST'])
def predict():
    if request.method=='POST':
        features  = [
            float(request.form['Waste Generated']),
            float(request.form['Population Density']),
            int(request.form['Municipal Efficiency Score']),
            float(request.form['Cost of Waste Management']),
            int(request.form['Awareness Campaigns Count']),
            float(request.form['Landfill Capacity']),
            int(request.form['Year'])
        ]

        features = np.array(features).reshape(1,-1)
        prediction = model.predict(features)[0]
        prediction = round(prediction, 2)

        return render_template("index.html", prediction = f"{prediction: 2f}%")
    
if __name__ == "__main__":
    app.run(debug=True)