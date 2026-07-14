import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    inputs = [float(x) for x in request.form.values()]

    X = [np.array(inputs)]

    prediction = model.predict(X)
    y_hat = prediction[0]

    return render_template('index.html', prediction_text=f"Predicted Power Output: {y_hat: .2f} MW", orig_inputs=inputs)

if __name__ == '__main__':
    app.run(debug=True)
